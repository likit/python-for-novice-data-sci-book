import requests
import json
import pandas as pd
import click
import os
from datetime import datetime

url = 'https://covid19.ddc.moph.go.th/api/Cases/round-1to2-by-provinces'


def load_data():
    resp = requests.get(url)
    data = json.loads(resp.text)  # resp.text is a csv text in JSON format
    df = pd.DataFrame(data)
    return df


def to_file(format, df, split, filename):
    print_func = getattr(df, 'to_excel') if format == 'xlsx' else getattr(df, 'to_csv')
    if not split:
        print_func(f'{filename}.{format}', index=False)
    else:
        provinces = df.head()['province'].unique()
        folder_name = datetime.now().strftime('%Y%m%d')
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        for p in provinces:
            click.echo('save data from {} to a file..'.format(p))
            df = df[df['province'] == p].head()
            print_func = getattr(df, 'to_excel') if format == 'xlsx' else getattr(df, 'to_csv')
            file_path = os.path.join(folder_name, f'{p}.{format}')
            print_func(file_path, index=False)


@click.group()
def main():
    pass


@main.command()
@click.option('--dry', is_flag=True, default=False)
@click.option('--all/--head', default=False)
@click.argument('provinces', nargs=-1)  # takes a variable number of provinces
@click.pass_context
def display(ctx, provinces, all, dry):
    if dry:
        if provinces:
            click.echo('Only data from {} are downloaded.'.format(','.join(provinces)))
        else:
            click.echo('All data are downloaded.')
        return

    df = load_data()
    if provinces:
        flt_df = df[df['province'].isin(provinces)]
        if not all:
            flt_df = flt_df.head()
    else:
        if not all:
            flt_df = df.head()
    click.echo(flt_df)


@main.command()
@click.option('-f', '--format', type=click.Choice(['xlsx', 'csv'], case_sensitive=False), default='xlsx')
@click.option('--split', is_flag=True, default=False)
@click.argument('filename', default='data', type=str)
def save(filename, format, split):
    df = load_data()
    click.echo('saving to {}.'.format(format))
    to_file(format, df, split, filename)


if __name__ == '__main__':
    main()
