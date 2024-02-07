# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 18:59:15 2023

@author: shoki
"""

from uuid import uuid4
class Avto:
    __num_Avto=0
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km=km
        self.__id=uuid4()
        Avto.__num_Avto+=1
    @classmethod   
    def get_num_Avto(cls):
        return cls.__num_Avto
    
    def get_km(self):
        return self.__km
    def Id(self):
        return self.__id
    def __repr__(self):
        return f"{self.rang.title()} {self.make} {self.model}"
    
class Avtosalon:
    def __init__(self,name):
        self.ism=name
        self.avtolar=[]
    def __repr__(self):
        return f"{self.ism} Avtosaloni"  
    def __getitem__(self,index):
        return self.avtolar[index]
    def add_avto(self,*avto):
        for a in avto:
            if isinstance(a, Avto):
                self.avtolar.append(a)
    def __len__(self):
        return len(self.avtolar)
    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat
    def __call__(self,*qiymat):
        if qiymat:
            for a in qiymat:
                self.add_avto(a)
        else:
            return [avto for avto in self.avtolar]
    def __add__(self,b):
        
        if isinstance(b,Avtosalon):
            yangi_salon=Avtosalon(f"{self.ism} {b.ism}")
            yangi_salon.avtolar=self.avtolar+b.avtolar
            return yangi_salon
        elif isinstance(b, Avto):
            self.add_avto(b)
            
    
class Shaxs:
    odamlar_soni=0
    __odamlar_soni=0
    def __init__(self,ism,familya,t_yil,ID):
        self.name=ism
        self.surname=familya
        self.t_yil=t_yil
        self.__ID=ID
        Shaxs.odamlar_soni+=1
        Shaxs.__odamlar_soni+=1
    @classmethod
    def get_odamlar(cls):
        return cls.__odamlar_soni
    def get_info(self):
        """Shaxsning malumotlarini chiqaradi"""
        return f"{self.surname} {self.name} {self.t_yil}-yilda tug'ilgan"
    def get_age(self,yil):
        """Hozirgi yilni kiritasiz va bu metod yosh qaytaradi"""
        return yil-self.t_yil
    def get_ID(self):
        return self.__ID
    def __repr__(self):
        return f"{self.surname} {self.name} {self.t_yil}-yilda tug'ilgan"
    def __le__(self,a1):
        if self.t_yil<=a1.t_yil:
            return f"{self.name} kichik yoki teng {a1.name}dan"
        else:
            return f"{a1.name} katta {self.name}dan"
    def __lt__(self,a1):
        if self.t_yil<a1.t_yil:
            return f"{a1.name} kichik {self.name}dan"
    

class dost:
    __num=0
    def __init__(self,ism,t_yil,manzil,yosh):
        self.ism=ism
        self.t_yil=t_yil
        self.manzil=manzil
        self.yosh=yosh
        dost.__num+=1
#   def __str__(self):
#        return f"{self.ism} {self.t_yil}-yilda {self.manzil}da tug'ilgan"
    def __repr__(self):
        return f"{self.ism} {self.t_yil}-yilda {self.manzil}da tug'ilgan"
    def __le__(self,y):
        return self.yosh<=y.yosh
    def __lt__(self,y):
        return self.yosh<y.yosh
    def __eq__(self, o):
        return self.yosh==o.yosh
    
    
class Fan:
    def __init__(self,nomi):
        self.nomi=nomi
        self.studentlar=[]
    def add_student(self,*student):
        for a in student:
            self.studentlar.append(a)
    def sub_studen(self,student):
        self.studentlar.remove(student)
    def __getitem__(self,i):
        return self.studentlar[i]
    def __setitem__(self,i,q):
        self.studentlar[i]=q
    def __repr__(self):
        return f"{self.nomi} fani"
    def __len__(self):
        return len(self.studentlar)
    def __add__(self,Q):
        self.add_student(Q)
    def __sub__(self,Q):
        self.sub_studen(Q)
    def __call__(self,*qiymat):
        if qiymat:
            for q in qiymat:
                if q in self.studentlar:
                    return f"{q} {self.nomi} fanida o'qiydi"
                else:
                    return f"{q} {self.nomi} fanida o'qimaydi"
        else: 
            return [x for x in self.studentlar]
    


###   dastur35 uchun Classlar

class Car:
    def __init__(self,kompanya,model,rang,km=0,narh=None):
        self.kompanya=kompanya
        self.model=model
        self.rang=rang
        self.narh=narh
        self.__km=km
    def get_make(self):
        return self.kompanya
    def add_km(self,km):
        if km>=0:
            self.__km+=km
        
            
        else:
            raise ValueError("km manfiy bo'lmaydi")
    def new_narh(self,a):
        self.narh=a
                
    def get_km(self):
        return self.__km
    def get_info(self):
        if self.narh==None:
            return f"{self.kompanya}: {self.rang.title()} {self.model}. {self.__km} km yurgan"
        else:
            return f"{self.kompanya}: {self.rang.title()} {self.model}. {self.__km} km yurgan. Narxi:{self.narh}"
    
    
    
    