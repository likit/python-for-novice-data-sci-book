## Level

* basic

## Prerequisite

* dictionary
* dictionary built-in methods
* iteration
* class

## Skill required

* สามารถอ่านข้อมูลจาก dictionary และใช้ฟังก์ชั่นพื้นฐานได้
* สร้าง class ได้

## Problem

1. จากข้อมูลที่ให้ จงสร้าง class เพื่อรับค่าตั้งต้นเป็น nuceotide sequence และสร้าง method composition() เพื่อคำนวณหา percent composition ของ nucleotide ใน sequence และเมื่อใช้คำสั่ง str() กับ instance ของ class นี้ให้แสดงผลดังด้านล่าง ทั้งนี้ลำดับของแถวสามารถสลับที่ได้

```
A: AAAAAAAA 26.7%
G: GGGGGGGGGGG 36.7%
T: TTTTT 16.7%
C: CCCCCC 20.0%
```

## Test Code

```Python
>>> ncomp = NucleotideComp('AGTGGCCGTGTGAAGAGAGTGCCAACCAGT')
>>> ncomp.composition()
{'A': 26.7, 'G': 36.7, 'T': 16.7, 'C': 20.0}

>>> print(ncomp)

A: AAAAAAAA 26.7%
G: GGGGGGGGGGG 36.7%
T: TTTTT 16.7%
C: CCCCCC 20.0%


```

2. เขียนโปรแกรมให้ตรวจสอบหากพบว่า nucleotide ที่ให้มาไม่ใช่ ATGC หรือ ATGU ให้ raise SequenceError exception ดังตัวอย่างด้านล่าง

## Test Code

```Python
>>> ncomp = NucleotideComp('thisisafakestring')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.SequenceError: Non-nucleotide characters are given.
```
