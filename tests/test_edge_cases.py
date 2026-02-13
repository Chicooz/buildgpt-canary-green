import unittest

class TestEdgeCases(unittest.TestCase):
    def test_empty_input(self):
        response = self.client.post('/your-endpoint', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()