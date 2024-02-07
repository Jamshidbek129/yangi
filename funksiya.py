# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:27:48 2023

@author: shoki
"""

def avto_info(kompaniya,modeli,yili,rangi,narxi=None):
    """Bu funksiya avtomobillar haqida malumot chiqaradi"""
    avto={'kompaniya':kompaniya,
          'model':modeli,
          'yil':yili,
          'rang':rangi,
          'narx':narxi}
    return avto


def avto_kirit():
    """foydalanuvchi avto_info funkisayi yordamida malumotlar kiritadi"""
    avtolar=[]
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting: ")
        kompaniya=input("Kompaniya nomi: ")
        modeli=input("Avtomobil modeli: ")
        yili=int(input("Yili: "))
        rangi=input("Rangi: ")
        avtolar.append(avto_info(kompaniya, modeli, yili, rangi))
        javob=input("Yana mashina qo'shamizmi?(ha\yoq) ")
        if javob=='yoq':
            break
    return avtolar

def info_print(avto_info):
    """Bu funksiya avto_info va avto_kiritni birlashtiradi"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya']}."
          f"Narxi: {avto_info['narx']}")
    return avto_info


def DATA(a,b):
    print("Salom Jamshidbek.Xush kelibsiz! ")
    print("Kiritgan soningizni darajaga oshirib beraman")
    a=int(input("Son kiriting: "))
    b=int(input("Daraja kiriting: "))
    return print(a**b) 

def fibona(n):
    a=[]
    a1=int(input("Massivning 1-elementini kiriting: "))
    a2=int(input("Massivning 2-elementini kiriting: "))
    a.append(a1)
    a.append(a2)
    for i in range(n-2):
        b=a[i]+a[i+1]
        a.append(b)
    print(a)
    return a




# dastur 34 uchun

def name(ism,familya):
    return f"{ism} {familya}".title()


def aylana_yuzi(r,pi=3.14159):
    return pi*r**2

def aylana_perimetri(r,pi=3.14159):
    return 2*pi*r

#man duzganim
def tub(n):
    m=n//2+1
    if n==2 or n==3:
        return True
    elif n<2:
        return False
    else:
        for i in range(m):
            if n%(i+2)==0:
              
                return False
           
        return True


#saytdan olganim
def tubSonmi(n):
    if n==2 or n==3: 
        return True
    if n%2==0 or n<2: 
        return False
    for i in range(3, int(n**0.5)+1, 2):   # faqat toq sonlarni tekshiramiz
        if n%i==0:
            return False   
    return True


# dastur34  AMALIYOT
def Max(a,b,c):
    return max(a,b,c)


def katta_harf(A):
    for i in range(len(A)):
        
        A[i]=A[i].capitalize()
    return A


def juft_son(A):
    B=[]
    m=0
    for i in range(len(A)):
        i=i-m
        if A[i]%2==0:
            x=A.pop(i)
            B.append(x)
            m+=1
           
    return B

def fibonada_bormi(a):
    m=1
    n=2
    l=1
    while l:
        x=m+n
        m=n
        n=x
       # print(x,end="  ")
        if x==a or a==1 or a==2:
            l=0
            return True
        elif x>a:
            l=0
            return False
