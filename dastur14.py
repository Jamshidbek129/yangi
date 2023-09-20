# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:41:51 2023

@author: shoki
"""
car0={"model":"cobalt",
     "rang":"oq",
     "yil":2021,
     "km":10000,
     "narx":200,
     "karobka":"mexanik"
     }
car1={"model":"nexia2",
     "rang":"malochniy",
     "yil":2012,
     "km":170000,
     "narx":60,
     "karobka":"mexanik"
     }
car2={"model":"gentra",
     "rang":"qora",
     "yil":2023,
     "km":11000,
     "narx":208,
     "karobka":"avtomat"
     }
cars=[car1,car2,car0]
for car in cars:
    print(f"{car['model']} "
          f"{car['km']}km yurgan,"
          f"{car['yil']}=yil, {car['rang']} rangda,{car['karobka']} karobka, "
          f"{car['narx']} mln so'm")



print(cars[0]["model"])
print(f"{cars[2]['rang']} {cars[2]['model']}")



cobaltlar=[]
for n in range(10):
    new_car={
    'model':'cobalt',
    'rang':None,
    'km':0,
    'narx':None,
    'yil':2023,
    'karobka':'mexanik'
    
}
    cobaltlar.append(new_car)
    

#for a in cobaltlar:
#    print(a)


for a in cobaltlar[:5]:
    a['rang']='oq'
    
for a in cobaltlar[5:10]:
    a['rang']='qora'
    

for a in cobaltlar[3:7]:
    a['karobka']='avtomat'



#for a in cobaltlar:
#    print(a)

for b in cobaltlar:
    if b['karobka']=='avtomat':
        b['narx']=210
    else:
        b['narx']=200
        
for a in cobaltlar:
    print(a)

dasturchilar={
    "Jamshid":['C++' , 'python'],
    "Farhod":['C++'],
    "Zafarbek":['Java' , 'python' ,'C++' , 'HTML']
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f"{til}  " , end='')

print('\n')


hamkasblar={
    'Jahongir':{
        'familya':'Rustamov',
        't_yil':2004,
        'manzil':'TATUUF',
        'tillar':['C++','Python']
        },
    'Oybek':{
        'familya':'Eshonqulov',
        't_yil':2004,
        'manzil':'TATU',
        'tillar':['C++']
        },
    'Zafarbek':{
        'familya':'Komuljonov',
        't_yil':1999,
        'manzil':"TATUUF",
        'tillar':['Java' , 'python' ,'C++' , 'HTML']
        }
    
    }

for a,b in hamkasblar.items():
    print(f"\n{a} {b['familya']}"
          f" {b['t_yil']}-yilda tug'ilgan.\n"
          f"Manzili: {b['manzil']} \n"
          "Quyidagi daturlash tillarini biladi: ")
    for c in b['tillar']:
        print(c)



#########   AMALIYOT >>>>>>>>>


m1={
    'ism':'Muhammad(s.a.v)',
    't_joy':'Makka',
    't_yil':571
    }

m2={
    'ism':'Ronaldo',
    't_joy':'Portugaliya',
    't_yil':1985
    }

m3={
    'ism':'Jamshid',
    't_joy':'Xorazm',
    't_yil':2004
    }


mashhurlar=[m1,m2,m3]
for a in mashhurlar:
    print(f"\n{a['ism']} {a['t_yil']}-yilda {a['t_joy']}da tavallud topgan")


l1={
    'ism':'Abu Abdulloh Muhammad ibn Ismoil',
    't_yil':810,
    't_joy':'Buxoro',
    'asarlar':['Al-adab al-mufrad','Al-jome as-sahih ',
               'Al-tarix al-kabir']}
l2={
    'ism':'Abdulla Qodiriy',
    't_yil':1894,
    't_joy':'Toshkent',
    'asarlar':['O\'tgan kunlar','Mehrobdan chayon','Obid ketmon']}
l3={
    'ism':'Alisher Navoiy',
    't_yil':1441,
    't_joy':'Hirot',
    'asarlar':['Xamsa','Lison ut-Tayr','Mahbob Al-Qulub']}


mashhurlar2=[l1,l2,l3]
for b in mashhurlar2:
    print(f"\n{b['ism']} {b['t_yil']}-yilda {b['t_joy']}da tavallud topgan.\n"
          "Quyidagi asarlarni yozgan:")
    for c in b['asarlar']:
        print(c,end=' ')
    print('\n')
kinolar={
    'Farhod':['Ishani','Titanik','Jumong'],
    'Abbos':['Samolar balandda','Xatiko','Xalq'],
    'Jamshidbek':['Qasoskorlar','Olamga nur sochgan oy','Afsungar']
    }
for a, b in kinolar.items():
    print(f"\n{a}ning sevimli filmlari:")
    for c in b:
        print(c)
    


davlatlar={
    'O\'zbekiston':{
        'poytaxt':'Toshkent',
        'aholisi':36,
        'pul birligi':'so\'m'},
    'Rossiya':{
        'poytaxt':'Moskva',
        'aholisi':152,
        'pul birligi':'rubl'},
    'AQSh':{
        'poytaxt':"Washington",
        'aholisi':405,
        'pul birligi':"dollor"}
    }
    
for a, b in davlatlar.items():
    print(f"\n{a}ning poytaxti {b['poytaxt']}.\n"
    f"Aholisi:{b['aholisi']}mln kishi.\n"
    f"Pul birligi: {b['pul birligi']}.")
davlatlar={
    'O\'zbekiston':{
        'poytaxt':'Toshkent',
        'aholisi':36,
        'pul birligi':'so\'m'},
    'Rossiya':{
        'poytaxt':'Moskva',
        'aholisi':152,
        'pul birligi':'rubl'},
    'AQSh':{
        'poytaxt':"Washington",
        'aholisi':405,
        'pul birligi':"dollor"}
    }
    
for a, b in davlatlar.items():
    print(f"{a}ning poytaxti {b['poytaxt']}.\n"
    f"Aholisi:{b['aholisi']}mln kishi.\n"
    f"Pul birligi: {b['pul birligi']}.\n")
    
    
f=input("Davlat nomini kiriting: ")
if f in davlatlar:
    a=davlatlar[f]
    
    print(f"{f}ning poytaxti {a['poytaxt']}.\n"
        f"Aholisi:{a['aholisi']}mln kishi.\n"
        f"Pul birligi: {a['pul birligi']}.\n")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q.")
    
    










