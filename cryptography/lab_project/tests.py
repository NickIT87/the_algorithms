import unittest
from Ciphers import CAESAR, TRITEMIUS


class TestCaesarCipher(unittest.TestCase):

    cipher_UA = CAESAR(key=12, alpha="UA")
    cipher_EN = CAESAR(key=3, alpha="EN")
    data_err_msg = "key must be Integer, greater than 0 and less than ABC length!"
    data_invalid_keys = [0, 123, '12']

    def test_encription(self):
        self.assertEqual(self.cipher_UA.enc("Шифр Цезаря"), 'етвяіґосїяи')
        self.assertEqual(self.cipher_EN.enc("abc"), 'def')
            
    def test_decription(self):
        self.assertEqual(self.cipher_UA.dec(self.cipher_UA.enc("Шифр Цезаря")), 'шифр цезаря')
        self.assertEqual(self.cipher_EN.dec(self.cipher_EN.enc("Caesar cipher")), 'caesar cipher')

    def test_key_validation(self):
        for test_key in self.data_invalid_keys:
            with self.assertRaises(ValueError, msg=self.data_err_msg):
                CAESAR(key=test_key, alpha="EN")
            


class TestTritemiusCipher(unittest.TestCase):

    cipher_UA = TRITEMIUS(key=12, alpha="UA")
    cipher_EN = TRITEMIUS(key=12, alpha="EN")
    data_err_msg = "key must be Integer, greater than 0 and less than ABC length!"
    data_invalid_keys = [0, 123, '12']

    def test_encription(self):
        self.assertEqual(self.cipher_UA.enc("Шифр Тритеміуса"), 'етвяіаятаошуб ї')
        self.assertEqual(self.cipher_EN.enc("Tritemius cipher"), 'ecueqyufdlouatqc')

    def test_decription(self):
        self.assertEqual(self.cipher_UA.dec(self.cipher_UA.enc("Шифр Тритеміуса")), 'шифр тритеміуса')
        self.assertEqual(self.cipher_EN.dec(self.cipher_EN.enc("Tritemius cipher")), 'tritemius cipher')

    def test_key_validation(self):
        for test_key in self.data_invalid_keys:
            with self.assertRaises(ValueError, msg=self.data_err_msg):
                TRITEMIUS(key=test_key, alpha="EN")


if __name__ == '__main__':
    unittest.main()