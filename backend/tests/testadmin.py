import unittest
from app import app

class AdminPanelTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_admin_dashboard_access(self):
        # First, simulate login
        self.client.post('/adminlogin', data={
            'username': 'admin',
            'password': 'admin'
        }, follow_redirects=True)

        # Then try accessing the dashboard
        response = self.client.get('/admin-dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Panel', response.data)

    def test_manage_posts_page(self):
        # Login first
        self.client.post('/adminlogin', data={
            'username': 'admin',
            'password': 'admin'
        }, follow_redirects=True)

        # Access manage posts
        response = self.client.get('/manage-posts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Posts', response.data)

    def test_manage_users_page(self):
        # Login first
        self.client.post('/adminlogin', data={
            'username': 'admin',
            'password': 'admin'
        }, follow_redirects=True)

        # Access manage users
        response = self.client.get('/manage-users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Users', response.data)

if __name__ == '__main__':
    unittest.main()
