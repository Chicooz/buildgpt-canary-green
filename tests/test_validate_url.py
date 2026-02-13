import unittest
from src.validate_url import is_valid_url

class TestValidateUrl(unittest.TestCase):
    def test_valid_urls(self):
        self.assertTrue(is_valid_url('http://example.com'))
        self.assertTrue(is_valid_url('https://example.com'))
        self.assertTrue(is_valid_url('http://www.example.com'))

    def test_invalid_urls(self):
        self.assertFalse(is_valid_url('ftp://example.com'))
        self.assertFalse(is_valid_url('http:/example.com'))
        self.assertFalse(is_valid_url('example.com'))

if __name__ == '__main__':
    unittest.main()
