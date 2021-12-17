# Control Flow

## Conditional control

ในการเขียนโปรแกรมโดยส่วนใหญ่ต้องมีการออกแบบตรรกะหรือ logic ของโปรแกรมเพื่อให้คอมพิวเตอร์สามารถตอบสนองและตัดสินใจได้จากข้อมูลที่เข้ามา (input)
ใน Python เราสามารถใช้ logical operator ร่วมกับคำสั่ง if, elif และ else เพื่อกำหนด logic ของโปรแกรมได้ดังนี้

### คำสั่ง IF

คำสั่ง IF เป็นคำสั่งที่ใช้กำหนดกรอบของชุดคำสั่งที่ตามให้รันเมื่อ expression เป็นจริงเท่านั้น เช่น


```Python

if len([23, 45, 56]) == 3:
    print('This list has three items.')  # this line will be executed.

if len('hello,world') == 3:
    print('This string has three characters')  # this line will not be executed.
```

เราสามารถใช้ Boolean operator กับคำสั่ง IF เพื่อประเมินเงื่อนไขที่ซับซ้อนได้ดังตัวอย่าง


```Python
firstname = 'Jane'
lastname = 'Doe'

if firstname != '' and lastname != '':
    print(f'Your initial is {firstname[0]}.{lastname[0]}.')  # 'Your initial is J.D.'
```

### คำสั่ง ELSE

คำสั่ง ELSE จะใช้ในการกำหนดกรอบของชุดคำสั่งที่จะทำงานเมื่อเงื่อนไขใน IF เป็นเท็จ เช่น

```Python
firstname = 'Jane'
lastname = ''

if firstname != '' and lastname != '':
    print(f'Your initial is {firstname[0]}.{lastname[0]}.')
else:
    print(f'You need to provide the firstname and the lastname.') # this line is executed.
```

### คำสั่ง ELIF

ชุดคำสั่งที่อยู่ถัดจาก ELIF จะทำงานเมื่อเงื่อนไขใน IF ก่อนหน้าเป็นเท็จและเงื่อนไขใน ELIF นั้นเป็นจริง เช่น

```Python
work_experience = 18

if work_experience < 5:
    print('You are a rookie.')
elif work_experience < 10:
    print('You are a junior.')
elif work_experience < 20:
    print('You are a senior.')
else:
    print('You are a master.')
    
    
# 'You are a senior.'


```

ลองเปรียบเทียบกับคำสั่ง IF ในตัวอย่างต่อไปจะเห็นความแตกต่างของการใช้ elif และ nested if

```Python
work_experience = 18

if work_experience < 5:
    print('You are a rookie.')
if work_experience < 10:
    print('You are a junior.')
if work_experience < 20:
    print('You are a senior.')
else:
    print('You are a master.')
    

```

### แบบฝึกหัด

จงเขียนโปรแกรมให้คำนวณค่า BMI จากน้ำหนักและส่วนสูงและแปลผลดังต่อไปนี้

|Value|Interpretation|
|------------|----------|
|<18.5|Underweight|
|18.5 and <25| Normal |
|25.0 and <30| Overweight |
|>=30|Obesity|

## Loop

### While loop

คำสั่ง while ใช้สำหรับกำหนดกรอบชุดคำสั่งให้ทำงานวนไปตราบใดที่เงื่อนไขที่กำหนดเป็นจริง

```Python
legal_age = 20

age = int(input('Enter your age: '))

# this code snippet will run until the age is lesser than 20.
while age >= legal_age:
    print('You can drink. Next!')
    age = int(input('Enter your age: '))

```

เราสามารถใช้คำสั่ง break เพื่อออกจากลูปได้ก่อนที่เงื่อนไขที่กำหนดจะเป็นเท็จเช่น

```Python
legal_age = 20

age = int(input('Enter your age: '))

# this code snippet will run until the age is lesser than 20.
while age >= legal_age:
    print('You can drink. Next!')
    
    # the code will exit the while loop if the age is greater than 80. 
    if age >= 80:
        print('You are also too old to hit the club.')
        break
    age = int(input('Enter your age: '))

```


### For loop

คำสั่ง for เป็นคำสั่งที่ทำงานกับข้อมูลชนิดที่เรียกว่า **iterator** ซึ่งเป็นข้อมูลที่สามารถมีมากกว่า 1 รายการหรือเป็น Python object ที่มีคำสั่งพิเศษเพื่อกำกับการทำงานของคำสั่ง for
และนอกจากนั้นคำสั่ง for มักใช้ในการสั่งให้ **generator** สร้างข้อมูลใหม่อีกด้วย

ในบทนี้เราจะขอพูดถึงเฉพาะข้อมูลก่อน ข้อมูลชนิด iterator ได้แก่ string, tuple, list, dict เป็นต้น
โดยส่วนใหญ่เรามักใช้คำสั่งนี้ในการเข้าถึงข้อมูลทีละรายการจนหมด เช่น

```Python
super_cars = ['Maserati', 'Porsche', 'Benz', 'BMW', 'Lamborghini']

for sc in super_cars:
    print(f'{sc} is a super car.')

```

เราสามารถใช้คำสั่ง continue และ break ในการกำกับคำสั่ง for ได้ เช่น

```Python
super_cars = ['Maserati', 'Porsche', 'Benz', 'BMW', 'Lamborghini']

for sc in super_cars:
    if len(sc) == 3:
        break
    if sc.startswith('B'):
        continue  # skip the rest and go to the next item
    print(f'{sc} is a super car that does not start with B.')
    
```

สำหรับการเข้าถึงข้อมูลใน iterator มากกว่า 1 iterator พร้อมกัน เรามักใช้คำสั่ง range และ len ร่วมกันกับคำสั่ง for เช่น

```Python
names = ['Jane', 'Mark', 'Joe', 'Brad']

incomes = [34000, 54000, 60000, 123000]

for i in range(len(names)):
    print(f'{names[i]} earns {incomes[i]}.')
```

ทั้งนี้ Python มีฟังก์ชั่น enumerate ที่สามารถนำมาใช้แทนฟังก์ชั่น range กับ len ได้ เช่น


```Python
names = ['Jane', 'Mark', 'Joe', 'Brad']

incomes = [34000, 54000, 60000, 123000]

for i, name in enumerate(names):
    print(f'{name} earns {incomes[i]}.')
```

หรือเราอาจจะใช้ฟังก์ชั่น zip เพื่อจับคู่รายการใน iterator เข้าด้วยกัน เช่น

```Python
names = ['Jane', 'Mark', 'Joe', 'Brad']

incomes = [34000, 54000, 60000, 123000]

for name, inc in zip(names, incomes):
    # zip returns [('Jane', 34000), ('Mark', 54000)..]
    print(f'{name} earns {inc}.')
```

สำหรับฟังก์ชั่น zip เป็นตัวอย่างของฟังก์ชั่นที่เรียกว่า generator ที่จะทำงานก็ต่อเมื่อคำสั่ง for พยายามเข้าถึงข้อมูลในรายการต่อไป สังเกตได้จาก

```Python
names = ['Jane', 'Mark', 'Joe', 'Brad']

incomes = [34000, 54000, 60000, 123000]

print(zip(names, incomes))

# <zip object at 0x103365940> this is a generator function
```

คำสั่ง generator อย่างเช่น zip สามารถ assign ให้กับตัวแปรได้และนำไปใช้กับ for loop ได้ โดยคุณสมบัติหนึ่งของ generator คือจะจดจำตำแหน่งของรายการข้อมูลที่เข้าถึงล่าสุดไว้ได้

```Python
names = ['Jane', 'Mark', 'Joe', 'Brad']

incomes = [34000, 54000, 60000, 123000]

pair_gen1 = zip(names, incomes)
pair_gen2 = pair_gen1

for name, inc in pair_gen1:
    print(name, inc)
    break

for name, inc in pair_gen2:
    print(name, inc)
```

จากตัวอย่างข้างต้น หากเราพยายามเข้าถึงรายการข้อมูลใน pair_gen1 อีกครั้ง เราจะได้ empty list เนื่องจากรายการของข้อมูลได้ถูกเข้าถึงจนหมดแล้ว
โดยฟังก์ชั่น list เป็นฟังก์ชั่นที่สั่งให้ generator สร้างข้อมูลพร้อมกับสร้าง list ใหม่ สังเกตว่าทั้งฟังก์ชั่น list และคำสั่ง for ทำหน้าที่คล้ายกันในการสั่งให้ generator สร้างข้อมูล

```Python

names = ['Jane', 'Mark', 'Joe', 'Brad']

incomes = [34000, 54000, 60000, 123000]

pair_gen1 = zip(names, incomes)
pair_gen2 = pair_gen1

for name, inc in pair_gen1:
    print(name, inc)
    break

for name, inc in pair_gen2:
    print(name, inc)

print(list(pair_gen1)) # []
```

การใช้คำสั่ง for กับ iterator หรือ generator มีประโยชน์มากในการจัดการกับข้อมูลขนาดใหญ่ เช่นการอ่านข้อมูลไฟล์ เนื่องจากการอ่านข้อมูลจากไฟล์ที่มีขนาดหลาย gigabytes ในครั้งเดียวอาจจะทำให้หน่วยความจำเต็มได้
และโดยทั่วไปเรามักจะ process ข้อมูลทีละรายการ ดังนั้นการที่เราสามารถเข้าถึงข้อมูลเฉพาะส่วนที่ต้องใช้งานจึงลดระยะเวลาในการอ่านไฟล์และหน่วยความจำ เช่น


```Python

for i, line in enumerate(open('examples/control_flow/bmi_calculator.py')):
    if 'bmi' in line:
        print(f'[{i}]: {line}')

```

ฟังก์ชั่น open ในตัวอย่างข้างต้นสร้าง file object ซึ่งเป็นข้อมูลชนิด iterator เมื่อใช้กับคำสั่ง for จะคืนค่าในไฟล์ที่เป็น text file ครั้งละหนึ่งบรรทัด