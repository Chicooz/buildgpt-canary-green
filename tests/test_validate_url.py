import unittest
from src.validate_url import is_valid_url

class TestValidateUrl(unittest.TestCase):

    def test_valid_url(self):
        self.assertTrue(is_valid_url("http://example.com"))
        self.assertTrue(is_valid_url("https://example.com"))

    def test_invalid_url(self):
        self.assertFalse(is_valid_url("http:///example.com"))
        self.assertFalse(is_valid_url("example.com"))
        self.assertFalse(is_valid_url("http://"))

if __name__ == '__main__':
    unittest.main()
