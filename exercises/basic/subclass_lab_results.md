## Level

* basic

## Prerequisite

* class inheritance

## Skill required

* สามารถสร้าง class และ subclass ได้

## Problem

1. จงเขียนโปรแกรมเพื่อสร้างชนิดของข้อมูลโดยใช้ class ชื่อว่า LabResult เพื่อจัดเก็บข้อมูลการตรวจ โดยใช้ฟิลด์ข้อมูลต่อไปนี้

* วันที่ทดสอบ
* HN
* LAB NO.
* ชื่อการทดสอบ
* ผลการทดสอบ
* หน่วย
* ชื่อผู้รายงานผล

### LabResult Class
| Field |
|---------|
|test_datetime|
|HN|
|lab_no|
|test|
|result|
|unit|
|reporter|

และสร้าง method print_result เพื่อแสดงผลการตรวจดังตัวอย่าง

```Python

>>> res = LabResult(datetime.datetime.now(), '3400044', 101, 'gluc', 98, 'mg/dL', 'James')
>>> res.print_result()
98 mg/dL

```
2. จงสร้าง subclass ของ LabResult เพื่อใช้บันทึกผลการตรวจ RT-PCR เพื่อให้สามารถแสดงผลค่า Ct และการแปลผลได้ดังตัวอย่าง

```Python

>>> res = PCRResult(datetime.datetime.now(), '3400044', 102, 'COVID RT-PCR', 27, 'Ct', 'detected', 'James')
>>> res.print_result()
27 Ct => detected

```
