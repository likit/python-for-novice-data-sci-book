print('Welcome to the BMI calculator')
weight = input('Enter your weight(kg): ')
height = input('Enter your height(cm): ')

bmi = float(weight) / (float(height) * 0.01) ** 2

print(f'Your BMI is {bmi:.1f}.')

if bmi < 18.5:
    print('Eat more!')
elif bmi < 25:
    print('You are normal.')
elif bmi < 30:
    print('You should watch your weight.')
else:
    print('Eat less!')