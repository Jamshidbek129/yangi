# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:14:36 2023

@author: shoki
"""
cars={"model":"BMW","rang":'Qora'}

print(cars["model"])
print(cars["rang"])
en_uz={"Cow":"Sigir","Cat":"Mushuk","Dog":"It"}
print(en_uz["Cow"])
print(f"Mening sevimli mashinamning modeli {cars['model']}")
talaba={"ism":"jamshidbek shokirov","yosh":19,"t_yil":2004}
print(f"{talaba['ism'].title()}\
 {talaba['t_yil']}-yilda tug'ilgan\
 talaba {talaba['yosh']} yoshda")

talaba["Kurs"]=2
talaba["Fakultet"]="Dasturiy injenering"
talaba["ism"]="Ruxsora"

print(talaba)
talaba1={}
talaba1["ism"]="Jamshid Shokirov"
talaba1["yosh"]=19
talaba1["kurs"]=2
print(f"Talaba {talaba1['ism'].title()} {talaba['yosh']} yoshda va u \
{talaba1['kurs']}-kursda o'qiydi")
print(talaba1)
del talaba1['yosh']
print(talaba1)
uy_hayvoni=en_uz.get('Cat',"Bunday uy hayvoni mavjud emas")
print(uy_hayvoni)







