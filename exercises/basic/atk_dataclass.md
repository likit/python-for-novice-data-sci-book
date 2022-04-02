## Level

* basic

## Prerequisite

* built-in data types
* data classes

## Skill required

* สามารถสร้าง data class ได้

## Problem

จงเขียนโปรแกรมเพื่อสร้างชนิดของข้อมูลโดยใช้ data class ชื่อว่า ATKResult เพื่อจัดเก็บข้อมูลการตรวจ ATK โดยใช้ฟิลด์ข้อมูลต่อไปนี้

* วันที่ทดสอบ
* ชื่อผู้ป่วย
* ผลการตรวจ (positive, negative, error)
* ประวัติเสี่ยง (True, False)
* จำนวนครั้งการได้รับวัคซีน

| Field | Data type | Default |
|---------|---------|-----------|
|test_datetime|datetime||
|patient_name|str||
|result|str||
|risk|bool||
|vaccination|int|0|

โดยทดสอบการสร้าง data class ด้วย code ต่อไปนี้

```Python

res = ATKResult(datetime.datetime.now(), 'John Doe', 'positive', False)
print(res.patient_name)
print(res.result)

if res.risk and res.result == 'negative':
  print('You should stay home for at least 7 days.'

```

### Hints

ข้อมูลชนิดวันที่สามารถกำหนดได้โดยการ import datetime data type ด้วย code ต่อไปนี้

```Python

from datetime import datetime

```
