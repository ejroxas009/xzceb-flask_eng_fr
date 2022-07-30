import unittest
from machinetranslation import translator

class Testtranslator(unittest.TestCase):
    def testenglishToFrench(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')
    def test2englishToFrench(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')
    def testfrenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')
    def test2frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')
unittest.main()
    