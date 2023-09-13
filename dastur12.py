# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:14:36 2023

@author: shoki
"""
#cars={"model":"BMW","rang":'Qora'}

#print(cars["model"])
#print(cars["rang"])
#en_uz={"Cow":"Sigir","Cat":"Mushuk","Dog":"It"}
#print(en_uz["Cow"])
#print(f"Mening sevimli mashinamning modeli {cars['model']}")
#talaba={"ism":"jamshidbek shokirov","yosh":19,"t_yil":2004}
#print(f"{talaba['ism'].title()}\
# {talaba['t_yil']}-yilda tug'ilgan\
# talaba {talaba['yosh']} yoshda")

#talaba["Kurs"]=2
#talaba["Fakultet"]="Dasturiy injenering"
#talaba["ism"]="Ruxsora"

#print(talaba)
#talaba1={}
#talaba1["ism"]="Jamshid Shokirov"
#talaba1["yosh"]=19
#talaba1["kurs"]=2
#print(f"Talaba {talaba1['ism'].title()} {talaba['yosh']} yoshda va u \
#{talaba1['kurs']}-kursda o'qiydi")
#print(talaba1)
#del talaba1['yosh']
#print(talaba1)
#uy_hayvoni=en_uz.get('Cat',"Bunday uy hayvoni mavjud emas")
#print(uy_hayvoni)



####  AMALIYOT >>>>>>
print("\n")
dadam={
       "ism":'azamat',
       'familya':"quryozov",
       't_yil':1982,
       'viloyat':"xorazm"
       }
print(f"Dadamning ismi {dadam['ism'].title()}. U {dadam['t_yil']} -yilda \
 {dadam['viloyat'].title()} viloyatida tug'ilgan. \n")
s_taomlar={
    "dadam":"manti",
    "onam":"baliq",
    "sevinch":"go'mma",
    "sevila":"barak"
    }
print(f"Dadamning sevimli taomi {s_taomlar['dadam']}")
print(f"Onamning sevimli taomi {s_taomlar['onam']}")
print(f"Sevinchning sevimli taomi {s_taomlar['sevinch']}")
print(f"Sevilaning sevimli taomi {s_taomlar['sevila']}")


python_lugati={
    "int":"integer ya'ni butun sonlar to'plami",
    "str":"string ya'ni matn to'plami ",
    "print":"chop etish",
    "if":"tarmoqlanish operatori ma'nosi-agar",
    "elif":"tarmoqlanish operatori ma'nosi-aks holda agar",
    "else":"tarmoqlanish operatori ma'nosi-aks holda",
    "for":"takrorlanuvchi operator",
    "list":"ro'yxat",
    "tuple":"o'zgarmas ro'yxat",
    "append":"listga qiymat qo'shish"
    }
lugat=python_lugati.get(input("So'z kiriting: ").lower(),"Bunday narsa mavjud emas!")
print(lugat)
kalit=input("so'z kiriting: ")
if kalit.lower() in python_lugati:
    print(python_lugati[kalit.lower()])
else:
    print("Bunday narsa mavjud emas!")




























































