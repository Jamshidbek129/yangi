# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:57:06 2023

@author: shoki
"""

import funksiya
avto1=funksiya.avto_info("BMW", "I5", 2024, "qora")
funksiya.info_print(avto1)
print("Dastur tugadi")

import funksiya as funk
avto1=funk.avto_info("BMW", "I5", 2024, "qora",40000)
funk.info_print(avto1)
print("Dastur tugadi")

from funksiya import avto_info,info_print
avto1=avto_info("BMW", "I5", 2024, "qora",50000)
info_print(avto1)
print("dastur tugadi")


from funksiya import avto_info as ai , info_print as ip
avto1=ai("BMW", "I5", 2024, "qora",50000)
ip(avto1)
print("dastur tugadi")

### random >>>
import random as ran
### randint()
son=ran.randint(1, 100)
print(son)

### choice()
ismlar=['farhod','jamshidbek','jahongir']
ism=ran.choice(ismlar)
print(ism.title())
print(ran.choice(ism))


x=list(range(0,100,10))
print(x)
print(ran.choice(x))

##### shuffle()
a=list(range(11))
print(a)
ran.shuffle(a)
print(a)




 




















