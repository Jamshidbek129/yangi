# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:00:08 2024

@author: shoki
"""
import unittest
from Classlar import Car , Shaxs
class Cartest(unittest.TestCase):
    def setUp(self):
        self.make="BMW"
        self.km1=12000
       # self.km2=0
        self.narh=80000
        self.avto=Car("BMW","M5 F90","qora",12000,80000)
        self.avto2=Car("BMW","M5 F90","qora")
    def test_xususiyat(self):
        self.assertIsNotNone(self.avto.kompanya)
        self.assertIsNotNone(self.avto.model)
        self.assertIsNotNone(self.avto.rang)
        self.assertIsNone(self.avto2.narh)
        self.assertEqual(self.avto2.get_km(), 0)
        
    
    
    def test_metod(self):
        self.assertEqual(self.avto.get_make(),self.make)
        
        self.avto.add_km(10000)
        self.assertEqual(self.avto.get_km(), self.km1+10000)
        
        try:
            self.avto2.add_km(-10000)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
        
        self.avto2.new_narh(70000)
        self.assertEqual(self.avto2.narh, 70000)
        
    
    
######################### AMALIYOT    >>>>>>>>>>>>>>>>>>>>>
    
class ShaxsTest(unittest.TestCase):
    def setUp(self):
        self.inson1=Shaxs("Jamshidbek", "Shokirov", 2004, "AD0417816")
        self.inson2=Shaxs("Farhod", "Jumayazov", 2004, "AD0417815")
    def test_x(self):
        self.assertEqual(self.inson1.name,"Jamshidbek" ) 
        #self.assertEqual(self.inson2.ID, "AD0417815")
        
        self.assertEqual(2, Shaxs.get_odamlar())
        
unittest.main()       
        
# avto=Car("BMW","M5 F90","qora",12000,80000)
# avto2=Car("BMW","M5 F90","qora")
# print(avto2.get_info())