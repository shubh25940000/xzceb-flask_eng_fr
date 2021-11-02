import unittest
from translator import eng_to_french, french_to_eng

class testTranslate(unittest.TestCase):
    def test_eng_to_french(self):
        self.assertEqual(eng_to_french('Hello'), 'Bonjour')  # add assertion here
    def test_french_to_engl(self):
        self.assertEqual(french_to_eng('Bonjour'), 'Hello')  # add assertion here


if __name__ == '__main__':
    unittest.main()
