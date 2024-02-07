# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:49:21 2024

@author: shoki
"""

import datetime as dt
now=dt.datetime.now()
print("Boshlandi:")
bugun=dt.date.today()
a=bugun.day
b=bugun.month
c=bugun.year
for i in range(10):
    if(b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12):
        if  a<=31:
            print(dt.date(c,b,a))
        else:
            b+=1
            if b>12:
                c+=1
                b=1
                print("Ishladi\n")
            a=a-31
            print(dt.date(c,b,a))
    elif(b==4 or b==6 or b==9 or b==11):
        if  a<31:
            print(dt.date(c,b,a))
        else :
            b+=1
            if b>12:
                c+=1
                b=1
                print("Ishladi\n")
            a=a-30
            print(dt.date(c,b,a))
    elif  b==2:
        if dt.date(c,b,29):
            if a<30:
                print(dt.date(c,b,a))
            else:
                a=a-29
                b+=1
                if b>12:
                    c+=1
                    b=1
                    print("Ishladi\n")
                print(dt.date(c,b,a))
        else:
            if a<29:
                print(dt.date(c,b,a))
            else:
                a=a-28
                b+=1
                if b>12:
                    c+=1
                    b=1
                    print("Ishladi\n")
                print(dt.date(c,b,a))
    a+=7
    
Ramazon=dt.date(2024,3,11)
Qurbon_Hayiti=dt.date(2024,6,17)
now=dt.datetime.now()
print(f"Ramazonga {(Ramazon-now.date()).days} kun qoldi!")
print(f"Qurbon hayitiga {(Qurbon_Hayiti-now.date()).days} kun qoldi!")



import datetime as dt
a=int(input("Yil:"))
b=int(input("Oy:"))
c=int(input("Kun:"))
now=dt.datetime.now().date()
t_kun=dt.date(a,b,c)
farq=now-t_kun
second=farq.seconds//3600
print(f"Bu sanaga {farq.days} kun {second} soat bo'lgan.")




from re import match , findall
tel=input("Tel raqamingizni kiriting:")
andoza1="^9........"
andoza2="^33......."
andoza3="^77......."
andoza4="^88......."
if match(andoza1, tel) or match(andoza1, tel) or match(andoza1, tel) or match(andoza1, tel):
    print("Qabul qilindi!")
else:
    print("Raqam noto'g'ri formatda kiritildi!")
andoza_url="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
matn="Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI "
#Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

url=findall(andoza_url, matn)
print(url)