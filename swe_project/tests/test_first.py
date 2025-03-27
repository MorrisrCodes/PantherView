import unittest
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

    def test_create_post(self):
        # Simulate creating a post (assuming you have an endpoint for this)
        response = self.client.post('/create_post', data=dict(
            title='Test Post',
            content='This is a test post.'
        ))
        self.assertEqual(response.status_code, 201)  # Adjust based on your actual response
        self.assertIn(b'Post created successfully', response.data)  # Adjust based on your actual response

if __name__ == '__main__':
    unittest.main()