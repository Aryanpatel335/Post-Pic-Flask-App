import unittest
from data_processing import filter_data, sort_data

class TestDataProcessing(unittest.TestCase):

    def test_filter_data(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(filter_data(data, lambda x: x > 3), [4, 5])

    def test_sort_data(self):
        data = [3, 1, 4, 5, 2]
        self.assertEqual(sort_data(data), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
