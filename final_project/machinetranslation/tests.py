import unittest
from translator import french_to_english
from translator import english_to_french
class TestMyModule1(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_f2e1(self):
        self.assertNotEqual(french_to_english(0),0)
    def test_f2e1(self):
        self.assertNotEqual(french_to_english('None'),'')

class TestMyModule2(unittest.TestCase):
    def test_f2e1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_f2e1(self):
        self.assertNotEqual(english_to_french(0),0)   
    def test_f2e1(self):
        self.assertNotEqual(english_to_french('None'),'')
unittest.main()        