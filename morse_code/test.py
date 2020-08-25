import unittest

from main import text_to_morsecode


class TestMorseConvertor(unittest.TestCase):
    def test_sos_critical(self):
        self.assertEqual(text_to_morsecode("sos"), '...---...')


if __name__ == "__main__":
    unittest.main()


