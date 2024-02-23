import unittest
from app import app 

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '<h1>Hello World!<h1/>')

if __name__ == '__main__':
    unittest.main()
