# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 10:57:04 2023

@author: shoki
"""
#kun=input("Bugun qaysi kun?\n>>>")
#temp=int(input("havo harorati:\n>>>"))


#if( kun.lower()=="shanba" or kun.lower()=="yakshanba" )and temp>=40 :
#    print("Yopo boramiz!!!")
#elif( kun.lower()=="shanba" or kun.lower()=="yakshanba") and temp<=40:
#    print("Uyda dam olamiz!!!")
#else:
 #   print("Bugun o'qish kuni")
#narx=12000
#choy=True #True ni o'rniga 1 False ni  o'rniga 0 qo'ysa ham bo'ladi
#non=True
#salat=False
#if choy:
#    narx=narx+5000
#if non:
 #   narx=narx+3000
#if salat:
#    narx=narx+7000
#print(narx)
#menu=['palov','shashlik',"barak",'somsa','sho\'rva']
#ovqat=input("Nima ovqat yeysiz?\n>>>")
#if ovqat.lower() in menu:
#    print("Buyurtmangiz qabul qilindi!")
#else:
#    print("Bizda bunday ovqat mavjud emas.")
#print("manti" not in menu)#in ning teskarisi.
#

#menu=["shashlik","barak","somsa","sho'rva","palov"]
#buyurtmalar=[]
#n=int(input("Nechta taom buyurtma qilasiz?>>>"))
#for i in range(n):
#    buyurtmalar.append(input(f"{i+1}-taomni kiriting: "))
#for taom in buyurtmalar:
#    if taom.lower() in menu:
#        print(f"Menuda {taom} bor!")
#    else:
#        print(f"Menuda {taom} yo'q.")


#########AMALIYOT
a=int(input("Juft sion kiriting: "))
if a%2==0:
    print("Raxmat!")
else:
    print(f"{a} juft son emas.")
b=int(input("Yoshingizni kiriting: "))
if b<4 or b>60:
    print("Sizga kirish bepul!")
elif b>4 and b<18:
    print("Chipta narxi 10000 so'm.")
else:
    print("Chipta narxi 20000 so'm.")
print("2 ta son kiriting")
c=float(input("1-sonni kiriting: "))
d=float(input("2-sonni kiriting: "))
if c==d:
    print(f"{c}={d}")
elif c<d:
    print(f"{c}<{d}")
else:
    print(f"{c}>{d}")
mevalar=["anor","olma","banan","nok","shaftoli","xurmo","uzum","behi","o'rik"]
savat=[]
bor_mevalar=[]
yoq_mevalar=[]
n=int(input("Necha xil meva olasiz?"))
for i in range(n):
    savat.append(input(f"{i+1}-meva nomini kiriting: "))
for j in savat:
    if j.lower() in mevalar:
        print(f"{j.capitalize()} bizda bor!")
    else:
        print(f"{j.capitalize()} bizda yo'q.")
for i1 in savat:
    if i1.lower() in mevalar:
        bor_mevalar.append(i1)
    else:
        yoq_mevalar.append(i1)
if yoq_mevalar==[]:
    print("Siz so'ragan barcha mevalar do'konimizda bor!")
else:
    print("Quyidagi mevalar bizning do'konda mavjud emas.")
    for i2 in yoq_mevalar:
        print(i2.capitalize())
foydalanuvchilar=["jamshid","programmer","ruxsora","myhome","tony_stark"]
a4=input("Yangi login kiriting: ")
while a4:
    if len(a4)>=5:
        if a4.lower() in foydalanuvchilar:
            print("Bu login band!")
            a4=input("Yangi login kiriting: ")
        else:
            print("Welcome!")
            break
    else:
        print("Login 5ta elementdan kam bo'lmasligi kerak!")
        a4=input("Yangi login kiriting: ")
        
        
a5=int(input("Butun son kiriting: "))
for i1 in range(2,11):
    if a5%i1==0:
        print(f"{a5} soni {i1} ga qoldiqsiz bo'linadi.")




















