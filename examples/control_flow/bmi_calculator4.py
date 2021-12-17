print('Welcome to the BMI calculator')

weights = []
heights = []

weight = input('Enter your weight(kg): ')
height = input('Enter your height(cm): ')
weight = float(weight)
height = float(height)
while weight > 0 and height > 0:
    weights.append(weight)
    heights.append(height)
    weight = input('Enter your weight(kg): ')
    height = input('Enter your height(cm): ')
    weight = float(weight)
    height = float(height)

bmis = 0.0

for i, bmi in enumerate(map(lambda v: v[0] / (v[1] * 0.01) ** 2, zip(weights, heights))):
    bmis += bmi

    if bmi is not None:
        if bmi < 18.5:
            interpretation = 'Eat more!'
        elif bmi < 25:
            interpretation = 'You are normal.'
        elif bmi < 30:
            interpretation = 'You should watch your weight.'
        else:
            interpretation = 'Eat less!'
        print(f'Input number {i} has BMI = {bmi:.1f}. {interpretation}')

print(f'The average BMIs of this group is {bmis/len(weights):.1f}')
