## Level

* basic

## Prerequisite

* dictionary
* dictionary built-in methods
* iteration

## Skill required

* สามารถอ่านข้อมูลจาก dictionary และใช้ฟังก์ชั่นพื้นฐานได้

## Problem

1. จากข้อมูลที่ให้ จงเขียนโปรแกรมให้แสดงผลดังด้านล่าง ทั้งนี้ลำดับของแถวสามารถสลับที่ได้

```
A: AAAAAAAA
G: GGGGGGGGGGG
T: TTTTT
C: CCCCCC

```

2. จงเขียนโปรแกรมให้คำนวณสัดส่วนเป็นร้อยละ (percent composition) ของ nucleotide แต่ละชนิดดังตัวอย่าง

```
A: AAAAAAAA 26.7%
G: GGGGGGGGGGG 36.7%
T: TTTTT 16.7%
C: CCCCCC 20.0%
```

## Data

```Python
sequence = 'AGTGGCCGTGTGAAGAGAGTGCCAACCAGT'

```


# Hints

* ใช้ dictionary ในการนับจำนวนตัวอักษร โดยกำหนดตัวอักษรเป็น key และจำนวนนับเป็น value
* ใช้ฟังก์ชั่น get และกำหนดค่า default value มาช่วยในกรณีที่พบตัวอักษรนั้นเป็นครั้งแรกเพื่อแก้ปัญหา KeyError หรือ
* เขียนเงื่อนไขเพื่อตรวจสอบว่า key มีอยู่ใน dictionary แล้วหรือไม่ และสั่งให้โปรแกรมทำงานต่างกันทั้งสองกรณี
