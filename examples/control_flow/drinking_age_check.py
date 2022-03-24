legal_age = 20

age = int(input('Enter your age: '))

# this code snippet will run until the age is lesser than 20.
while True:
    if age <= 0:
        break
    if age >= legal_age:
        print('You can drink. Next!')
    else:
        print('You cannot drink')

    age = int(input('Enter your age: '))