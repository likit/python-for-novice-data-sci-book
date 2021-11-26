domains = {}
emails = {}

email = ''

while email != 'q':
    email = input('Enter your email: ')
    cnt = emails.get(email, 0) + 1
    emails[email] = cnt

    domain = email.split('@')[-1]
    dcnt = domains.get(domain, 0) + 1
    domains[domain] = dcnt

    print(f'You have registered {cnt} times.')
    print(f'People with your email domain have registered {dcnt} times.')
