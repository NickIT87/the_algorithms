import unittest
from Ciphers import CAESAR, TRITEMIUS


class TestCaesarCipher(unittest.TestCase):

    def test_UA_encription(self):
            cipher = CAESAR(key=12, alpha="UA")
            self.assertEqual(cipher.enc("Шифр Цезаря"), 'етвяіґосїяи')
            
    def test_UA_decription(self):
            cipher = CAESAR(key=12, alpha="UA")
            self.assertEqual(cipher.dec(cipher.enc("Шифр Цезаря")), 'шифр цезаря')


class TestTritemiusCipher(unittest.TestCase):

    def test_lower(self):
        #self.assertTrue('This is broken' in str(unittest.context.exception))
        pass


if __name__ == '__main__':
    unittest.main()