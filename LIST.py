# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:37:37 2023

@author: shoki
"""
A=[]
B=[]

n=int(input("Ro'yxatga nechta son kiritasiz: "))
for i in range(n):
    x=int(input(f"{i+1}-elementni kiriting: "))
    A.append(x)
print(f"Siz kiritgan ro'yxat: {A}")
print(f"Siz kiritgan ro'yxatni saralangani: {sorted(A)}")
for i in range(n-1):
    if A[i]>A[i+1]:
        m=A[i]-A[i+1]
        B.append(m)
    else:
        m=A[i+1]-A[i]
        B.append(m)
print(B)
a=max(B)
b=B.index(a)
print(A[b]+A[b+1])



