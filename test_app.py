from app import app

import unittest


class BasicTestCase(unittest.TestCase):
    """initial test. ensure flask was set up correctly"""

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_favicon(self):
        tester = app.test_client(self)
        response = tester.get('/static/favicon.png', content_type="image/png")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
