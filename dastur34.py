import unittest
import funksiya 
from funksiya import tubSonmi , Max , katta_harf , juft_son , fibonada_bormi

class Name_test(unittest.TestCase):
    def test_name(self):
        ism=funksiya.name("jamshidbek","shokirov")
        self.assertEqual("Jamshidbek Shokirov", ism)



class aylana(unittest.TestCase):
    def test_yuza(self):
        S=funksiya.aylana_yuzi(10,3.14159)
        self.assertAlmostEqual(S,314.159)
        
    def test_perimetr(self):
        P=funksiya.aylana_perimetri(5)
        self.assertAlmostEqual(P, 31.4159)



class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))
        



##############   AMALIYOT   >>>>>>>>>>>>


class Katta(unittest.TestCase):
    def test_katta_son(self):
        self.assertEqual(Max(1,2,3), 3)
        
    def test_katta_harf(self):
        A=["assalomu aleykum","valeykum assalom"]
        B=["Assalomu aleykum","Valeykum assalom"]
        self.assertEqual(katta_harf(A), B) 

class JuftSon(unittest.TestCase):
    def test_juft_son(self):
        A=juft_son([1,2,3,4,5,6,7,8,9,0])
        B=[2, 4, 6, 8, 0]
        self.assertEqual(A, B)
        
        
class fibonachchi(unittest.TestCase):
    def test_fibona_True(self):
        self.assertTrue(fibonada_bormi(1))
        self.assertTrue(fibonada_bormi(2))
        self.assertTrue(fibonada_bormi(8))
    def test_fibona_False(self):
        self.assertFalse(fibonada_bormi(4))
        self.assertFalse(fibonada_bormi(6))
        
unittest.main()


