## Level

* basic

## Prerequisite

* built-in data types
* math operators
* iteration

## Skill required

* สามารถอ่านข้อมูลจาก dictionary ได้
* สามารถเขียนโปรแกรมให้คำนวณทางคณิตศาสตร์ได้

## Problem

จากข้อมูลที่ให้ จงเขียนโปรแกรมให้คำนวณและรายงานจำนวนพนักงานในแต่ละตำแหน่งหลังจากบริษัททั้งสองได้ทำการควบรวมเป็นบริษัทเดียวกัน โดยไม่มีพนักงานคนใดลาออก

## Data

```Python
company_a = {'engineer': 20, 'accountant': 10, 'lawyer': 12, 'manager': 5}

company_b = {'architect': 8, 'engineer': 12, 'accountant': 5, 'salesperson': 6, 'marketing': 3}

```

จงแสดงผลลัพธ์ดังนี้

```
accountant: 15
architect: 8
engineer: 32
salesperson: 6
marketing: 3
lawyer: 12
manager: 5
```

## Hints

* เนื่องจากต้องนับตำแหน่งงานจากทั้งสอง dictionary ที่มีตำแหน่งงานไม่เหมือนกันบางส่วน ดังนั้นควรทำการรวมตำแหน่งงานทั้งหมดไว้ใน set ก่อนเนื่องจากเราไม่จำเป็นต้องนับซ้ำ
* จากนั้นใช้ตำแหน่งงานจาก set เรียกดูข้อมูลจาก dictionary เพื่อป้องกัน KeyError เนื่องจากสองบริษัทมีตำแหน่งงานต่างกัน ควรใช้ฟังก์ชั่น get ในการเรียกดูข้อมูลแทน
