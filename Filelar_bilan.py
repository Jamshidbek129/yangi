# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:28:03 2024

@author: shoki
"""

file=open("pi.txt")
PI=file.read()
print(PI,"\n")
file.close()


with open("pi.txt") as file:
    PI=file.read()
print(PI,"\n")


PI=PI.replace("\n","")
PI=PI.replace(" ","")
PI=float(PI)
print(PI,"\n")
with open("L.txt") as x:
    for l in x:
        print(l) 


with open("L.txt") as x:
    M=x.readlines()
M=[i.rstrip() for i in M]
print(M)


yangi_file="yangi-file.txt"
with open(yangi_file,"w") as file:
    file.write("salom"+" ")
    file.write(str(2004)+"\n")
    
with open(yangi_file,"a") as file:
    file.write("Valeykum salom ")    
    
import pickle
A1={"ism":"Jamshidbek","familya":"Shokirov","yil":2004}
A2={"ism":"Sevinch","familya":"Shokirova","yil":2007}
A3={"ism":"Sevila","familya":"Shokirova","yil":2011}


with open("pickle","wb") as file:
    pickle.dump(A1,file)
    pickle.dump(A2,file)
    pickle.dump(A3,file)
    
    
with open ("pickle","rb") as file:
    A1=pickle.load(file)
    A2=pickle.load(file)
    A3=pickle.load(file)
    
print(A1)
print(A2)
print(A3)   
    