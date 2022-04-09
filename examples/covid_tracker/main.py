import requests
import json
import pandas as pd
import click
import os
from datetime import datetime

url = 'https://covid19.ddc.moph.go.th/api/Cases/round-1to2-by-provinces'


def download_data():
    resp = requests.get(url)
    data = json.loads(resp.text)
    return pd.DataFrame(data)


def to_file(df, split, format, filename):
    folder_name = datetime.now().strftime('%Y%m%d')
    if split:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        provinces = df['province'].unique()
        for p in provinces:
            flt_df = df[df['province'] == p]
            write_func = getattr(flt_df, 'to_excel') if format == 'xlsx' else getattr(flt_df, 'to_csv')
            file_path = os.path.join(folder_name, f'{p}.{format}')
            write_func(file_path, index=False)

    write_func = getattr(df, 'to_excel') if format == 'xlsx' else getattr(df, 'to_csv')
    write_func(f'{filename}.{format}', index=False)


@click.group()
def main():
    pass


@main.command()
@click.option('--dry', is_flag=True)
@click.option('--all/--head', default=False)
@click.argument('provinces', nargs=-1)  # variable number of provinces
def display(all, provinces, dry):
    if dry:
        if provinces:
            click.echo('Displaying data from {}'.format(','.join(provinces)))
        else:
            click.echo('Data from all provinces will be displayed.')
        return
    df = download_data()
    if provinces:
        flt_df = df[df['province'].isin(provinces)]
    else:
        flt_df = df
    if all:
        print(flt_df)
    else:
        print(flt_df.head())


@main.command()
@click.option('--split', is_flag=True)
@click.option('--filename', type=str, default='demo')
@click.option('-f', '--format', type=click.Choice(['xlsx', 'csv'], case_sensitive=False), default='xlsx')
def save(split, format, filename):
    df = download_data()
    to_file(df, split, format, filename)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
