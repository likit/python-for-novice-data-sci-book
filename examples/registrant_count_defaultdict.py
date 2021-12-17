from collections import defaultdict

domains = defaultdict(int)
emails = defaultdict(int)

email = ''

while email != 'q':
    email = input('Enter your email: ')
    emails[email] += 1

    domain = email.split('@')[-1]
    domains[domain] += 1

    print(f'You have registered {emails[email]} times.')
    print(f'People with your email domain have registered {domains[domain]} times.')
