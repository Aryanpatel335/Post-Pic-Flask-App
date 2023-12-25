import unittest
from string_utils import reverse_string, capitalize_string

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")

if __name__ == '__main__':
    unittest.main()
