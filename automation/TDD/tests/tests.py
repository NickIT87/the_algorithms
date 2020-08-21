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
    def test_nitro_salt_returns_integer(self):
        self.assertEqual(nitro_salt(1000), 10)


if __name__ == "__main__":
    unittest.main()
