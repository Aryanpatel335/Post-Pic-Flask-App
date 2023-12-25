import unittest
from api_client import get_user, post_data

class TestApiClient(unittest.TestCase):

    def test_get_user(self):
        self.assertEqual(get_user(1), {"id": 1, "name": "John Doe"})

    def test_post_data(self):
        response = post_data({"key": "value"})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
