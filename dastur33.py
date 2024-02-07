# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:54:39 2024

@author: shoki
"""

yosh=input("Yoshingizni kiriting:")
try:
    yosh=int(yosh)
except:
    print("Siz butun son kiritmadingiz!")
else:
    print(f"Siz {2024-yosh}-yilda tug'ilgansiz")

# bu yerda ValueError sodir bo'ldi buni exceptni yoniga yozsa ham bo'ladi

yosh=input("Yoshingizni kiriting:")
try:
    yosh=int(yosh)
except ValueError:
    print("Siz butun son kiritmadingiz!")
else:
    print(f"Siz {2024-yosh}-yilda tug'ilgansiz")


# yana bitta xatolik bu ZeroDivisionError yani:
a=int(input("Son kiriting: "))
try:
    b=12/a
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas")
else:
    print(b)
    
    
# yana bitta xatolik bu IndexError yani:

sonlar=list(range(1,10))
try:
    print(sonlar[9])
except IndexError:
    print(f"Ro'yxatda {len(sonlar)} ta son bor. Siz indexni oshirib yubordingiz")
    
    
# yana bitta xatolik KeyError yani:

Fan={"nomi":"Matematika",
     "sinf":8,
     "talabalar":["Jamshidbek","Farhodjon","Jahongir"]
     }
key=input("Kalit so'zni kiriting: ")
try:
    print(Fan[key])
except KeyError:
    print("Kalit so'zni xato kiritdingiz!")



# yana bitta xatolik FileNotFoundError yani:

filename="__pycache__/jamshid.txt"
try:
    with open(filename) as file:
        x=file.read()
except FileNotFoundError:
    print(f"{filename} nomli fayl mavjud emas!")
else:
    print(x)
    

# pass hech nima bajarmay o'tib ketish

filename="__pycache__/jamshid.txt"
try:
    with open(filename) as file:
        x=file.read()
except FileNotFoundError:
    pass
else:
    print(x)












    
    
    
    
    
    
    
    
    