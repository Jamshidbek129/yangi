# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:34:45 2023

@author: shoki
"""
with open("pi.txt") as file:
    x=file.read()
#print(x)

#x=x.rstrip()
x=x.replace("\n", "")
x=x.replace(" ", '')
x=float(x)
print(x)
filename="__pycache__/jamshid.txt"
with open(filename) as file:
    y=file.readlines()
    
print(y)
y=[i.replace("\n","") for i in y]
print(y)
filename="yangi_file"

#  YANGI FILE YARATADI VA UNGA YOZADI
with open(filename,"w") as file:
    file.write("JARVIS"+"\n")
    file.write("ALTRON"+"\n")


#  MAVJUD FILEGA QO'SHADI YO'Q BO'LSA YANGIDAN YARATADI VA YOZADI

with open(filename,"a") as fayl:
    fayl.write("STARK"+"\n")
import pickle
talaba1={"ism":"Jamshidbek","familya":"Shokirov"}
talaba2={"ism":"Oybek","familya":"Eshonqulov"}
with open("talaba","wb") as X:
    pickle.dump(talaba1, X)
    pickle.dump(talaba2,X)
    
with open("talaba","rb") as Y:
    x1=pickle.load(Y)
    x2=pickle.load(Y)
print(x1)


###########   AMALIYOT   >>>>>>>>>>>>>
with open("L.txt") as X:
    x=X.read()
x=x.replace(" ","")
x=x.replace("\n", "")
x=float(x)
print(x)

with open("X","wb") as B:
    pickle.dump(x, B)
with open("X","rb") as B:
    x1=pickle.load(B)
print(x1)
    

def top(x):
    with open("pi_million_digits.txt") as A:
        y1=A.read()
    if x in y1:
        print("ha bor")
    else:
        print("yo'q ekan")
top("1809")


m="malumot"
def qoshish(y):
    with open(m,"a") as R:
        R.write(y+"\n")
ism=input("F.I.O \n>>>")
qoshish(ism)
telfon=input("tel \n>>>")   
qoshish(telfon)







