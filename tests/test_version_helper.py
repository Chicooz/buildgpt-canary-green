import unittest
from version_helper import get_version

class TestVersionHelper(unittest.TestCase):

    def test_get_version(self):
        self.assertEqual(get_version(), "1.0.0")

    def test_get_version_type(self):
        self.assertIsInstance(get_version(), str)

    def test_get_version_non_empty(self):
        self.assertTrue(len(get_version()) > 0)

if __name__ == '__main__':
