import unittest
from file_operations import read_file, write_file

class TestFileOperations(unittest.TestCase):

    def test_read_file(self):
        self.assertEqual(read_file("test.txt"), "Sample text")

    def test_write_file(self):
        write_file("test.txt", "New text")
        self.assertEqual(read_file("test.txt"), "New text")

if __name__ == '__main__':
    unittest.main()
