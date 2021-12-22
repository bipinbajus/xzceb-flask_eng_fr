import unittest
from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):
    """Test Translator"""
    def test_english_to_french_text(self):
        self.assertEqual(english_to_french('Hello'),"Bonjour")

    def test_english_to_french_not(self):
        self.assertNotEqual(english_to_french('Hello'),"Hello")

    def test_french_to_english_text(self):
        self.assertEqual(french_to_english('Bonjour'),"Hello")

    def test_french_to_english_not(self):
        self.assertNotEqual(french_to_english('Bonjour'),"Bonjour")

if __name__ == '__main__':
    unittest.main()
    