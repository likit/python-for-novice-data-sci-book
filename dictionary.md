# Dictionary

เป็นชนิดของข้อมูลที่เก็บข้อมูล key และ value โดย key จะจับคู่กับ value (mapping) แบบ 1:1 ทำให้การเรียกดูข้อมูลมีความรวดเร็วสูง แต่ข้อจำกัดคือ key ต้องไม่ซ้ำกัน (unique)

การสร้าง dictionary สามารถสร้างได้หลายวิธีดังนี้


```Python

d = dict()  # the built-in dict function
d = {}  # a literal form

d = dict(a=32, b=45, c='Mazda')
d = {'a': 32, 'b': 45, c: 'Mazda'}

```

นอกจากนั้นเรายังสามารถสร้าง dictionary จากลิสต์ของ tuple ได้ด้วย เช่น

```Python

d = dict([('a', 32), ('b', 45), ('c', 'Mazda')])

```

การเรียกดูข้อมูลสามารถทำได้หลายวิธีได้แก่

การเรียกดูข้อมูลด้วย key indexing

```Python

d['a']  # returns  32
d['x']  # KeyError

```

เรียกข้อมูลด้วย **get** method

```Python

d.get('a')  # returns 32
d.get('x')  # returns None
d.get('x', 100)  # returns 100 if 'x' is not a key 

```

การเพิ่มหรือแก้ไขข้อมูลทำได้โดยวิธีการ indexing

```Python

d['x'] = 100 # set x to 100
d['x']  # returns 100

d['x'] = 120 # set x to 120
d['x']  # returns 120

```

การอัพเดตข้อมูลจากอีก dictionary ทำได้โดยใช้ update method ตัวอย่างเช่น


```Python

a = {'b': 120, 'c': 450, 'd': 50}
b = {'a': 23, 'b': 45, 'x': 100}

a.update(b)  # a is now {'a': 23, 'b': 45, 'c': 450, 'd': 50, 'x': 100}

```

ข้อควรระวัง key ใน dictionary จะไม่เรียงตามตัวอักษรหรือตัวเลขแม้ว่าบางครั้งจะเหมือนว่าเรียงอย่างมีระบบก็ตาม


การนับจำนวนรายการใน dictionary สามารถทำได้โดยใช้ **len** function

```Python

d = {'b': 120, 'c': 450, 'd': 50}
len(d)  # returns 3 (number of items)

```

เราสามารถใช้ method ต่อไปนี้เพื่อแสดงข้อมูลใน dictionary โดยผลลัพธ์ที่ได้จะได้เป็นลิสต์ของรายการต่าง ๆ

### keys method
แสดง key ใน dictionary

```Python

d = {'b': 120, 'c': 450, 'd': 50}
d.keys()  # returns ['b', 'c', 'd']

```

### values method
แสดง value ใน dictionary

```Python

d = {'b': 120, 'c': 450, 'd': 50}
d.values()  # returns ['120', '450', '50']

```

### items method

```Python

d = {'b': 120, 'c': 450, 'd': 50}
d.items()  # returns [('b', 120), ('c', 450), 'd', 50]

```

เราสามารถทดสอบว่ามี key อยู่ใน dictionary โดยใช้ **in** operator

```Python

d = {'b': 120, 'c': 450, 'd': 50}

'b' in d  # returns True
'x' in d  # returns False

```

```

ตัวอย่างการเขียนโปรแกรมเพื่อนับจำนวนผู้เข้าร่วมประชุมตาม email โดยโปรแกรมสามารถสรุปจำนวนครั้งที่ผู้เข้าร่วมประชุมได้เข้าร่วมและจำนวนครั้งที่ผู้ใช้ email domain เดียวกันได้

ชื่อไฟล์ registrant_count.py

```

### Note

นอกจาก dictionary แล้วเรายังสามารถใช้ defaultdict จาก collections module เพื่อเก็บข้อมูลได้ โดยเราสามารถกำหนดค่าตั้งต้นของ value ได้ เช่น


```Python

from collections import defaultdict

d = defaultdict(int)  # default value is integer which is set to 0 by default

d['x']  # returns 0, even though x is not a key

d['y'] += 20
d.get('y') == 20  # returns True

```


### แบบฝึกหัด

- จากตัวอย่างในไฟล์ registrant_count.py จงใช้ defaultdict แทน dictionary

- จากตัวอย่างในไฟล์ registrant_count.py จงใช้ defaultdict ในการเก็บข้อมูล email ในแต่ละ domain ไว้ใน list เดียวกัน

