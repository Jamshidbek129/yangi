# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:26:13 2024

@author: shoki
"""

class hayvonlar:
    __num_hayvon=0
    def __init__(self,turi,soni,rangi):
        self.tur=turi
        self.son=soni
        self.rangi=rangi
        hayvonlar.__num_hayvon+=1
    @classmethod
    def get_son(cls):
        return f"{cls.__num_hayvon} xil hayvon bor"
    def chiqarish(self):
        return f"Bizning uyda {self.son} ta {self.rangi} {self.tur} bor"
    def __repr__(self):
        return self.tur
    def __call__(self):
        return f"{self.son} ta {self.tur} bor"
    def __lt__(self,y):
        if self.son>y.son:
            print(f"{self.tur}lar soni {y.tur}lar sonidan ko'p")
        else:
            print(f"{self.tur}lar soni {y.tur}lar sonidan kam")
    def __eq__(self, o):
        if self.son==o.son:
            print(f"{self.tur}lar soni {o.tur}lar soniga teng")
        else:
            print(f"{self.tur}lar soni {o.tur}lar soniga teng emas")
    def __ne__(self, o):
        return self.son!=o.son
    def __le__(self,o):
        return self.son<=o.son
class uy_hayvonlari(hayvonlar):
    def __init__(self,turi,soni,rangi,yoshi):
        super().__init__(turi, soni, rangi)
        self.yosh=yoshi
    def  chiqarish(self):
        return f"Bizning uyda {self.yosh} yoshli {self.son} ta {self.rangi} {self.tur} bor"
    
    
    
class oila:
    def __init__(self,nom):
        self.nomi=nom
        self.o_azolar=[]
    def add(self,*x):
        for i in x:
            self.o_azolar.append(i)
    def __getitem__(self,i):
        return self.o_azolar[i]
    def __setitem__(self,index,qiymat):
        self.o_azolar[index]=qiymat
    def __len__(self):
        return len(self.o_azolar)
    
    
    
class sinf:
    def __init__(self,nomi):
        self.nom=nomi
        self.oquvchilar=[]
    def __repr__(self):
        return self.nom
    def add(self,*x):
        for i in x:
            self.oquvchilar.append(i)
    def __add__(self,o):
        yangi_sinf=sinf(self.nom+o.nom)
        
        return (yangi_sinf)
    
A=sinf("A")
B=sinf("B")
print(A+B)

           
        
Azamat=oila("Azamat oilasi")    
Azamat.add("Azamat","Gulshan","Jamshid","Sevinch","Sevila")
print(Azamat[2])
Azamat[2]="Jamshidbek"
print(Azamat[:])




sher=hayvonlar("sher", 1, "sariq")
sigir=uy_hayvonlari("sigir", 4, "qizil", 1)
print("\n",sigir.chiqarish())
print(sher.chiqarish())

