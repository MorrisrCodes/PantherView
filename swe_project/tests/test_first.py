import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from first import create_app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    # Comment out or remove this test if /create_post does not exist
    def test_create_post(self):
        response = self.client.post('/create_post', json={
            'title': 'Test Post',
            'content': 'This is a test post.'
        })
        self.assertEqual(response.status_code, 201) 
        self.assertIn(b'Post created successfully', response.data) 

if __name__ == '__main__':
    unittest.main()