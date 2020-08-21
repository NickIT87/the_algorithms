import unittest
import sys, os

from main import *

#sys.path.append(os.getcwd())
#print(sys.path[0])
#print("\n")
#print(os.getcwd())
#print("\n")
#print(len(sys.path))

class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000), int)


if __name__ == "__main__":
    unittest.main()
