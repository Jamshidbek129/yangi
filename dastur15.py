# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:49:23 2023

@author: shoki
"""

name=input("Ismingizni kiriting: ")
savol=f"Salom {name.title()}. Yoshingizni kiriting: "
yosh=int(input(savol))   



savol="Istalgan son kiriting\n"
savol+="(Dasturni tugatish uchun 'a' ni bosing): "
qiymat=''
while qiymat!='a':
    qiymat=input(savol)
    if qiymat!='a':
        print(float(qiymat)**2)
print("Dastur tugadi")
    



savol="Istalgan son kiriting\n"
savol+="(Dasturni tugatish uchun 'a' ni bosing): "
qiymat=''
a=True
while a:
    qiymat=input(savol)
    if qiymat!='a':
        print(float(qiymat)**2)
    else:
        a=False
print("Dastur tugadi")




savol="Istalgan son kiriting\n"
savol+="(Dasturni tugatish uchun 'a' ni bosing): "
qiymat=''
while True:
    qiymat=input(savol)
    if qiymat!='a':
        print(float(qiymat)**2)
    else:
        break
print("Dastur tugadi")



sonlar=list(range(1,11))
for son in sonlar:
    if son==5:
        break
    print(f"{son}ning kvadrati {son**2}ga teng")
print("Dastur tugadi")  
    
    
    
sonlar=list(range(1,11))
for son in sonlar:
    if son==5:
        continue
    print(f"{son}ning kvadrati {son**2}ga teng")
print("Dastur tugadi")  


son=0
while son<10:
    son+=1
    if son%2==0:
        continue
    else:
        print(son,end=' ')





#######     AMALIYOT   >>>>>>>>>>
kitoblar=[]
a=True
i=1
while a:
    b=input(f"\n{i}-Sevimli filmingizni nomini kiriting:\
 (dasturni to'xtatish uchun 'f' ni bosing) ")
    i+=1
    if b!='f':
        kitoblar.append(b.title())
    else:
        a=False

print(kitoblar)



while True:
    print("\nDasturni to'xtatishni xoxlasangiz 'exit' yoki 'quit' deb yozing")
    b=input("Yoshingizni kiriting: ")
    if b=='exit' or b=='quit':
        break
    else:
        b=int(b)
        if b<=7:
            print("Sizga chipta narxi 2000 so'm")
        elif 7<b<=18:
            print("Sizga chipta narxi 3000 so'm")
        elif 18<b<=65:
            print("Sizga chipta narxi 10000 so'm")
        else:
            print("Siz uchun chipta bepul")



savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    else:
        if int(qiymat)<0:
            continue
    
        else:
            ildiz = float(qiymat)**(0.5)
            print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
    

