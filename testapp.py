
import unittest
import app as app

class TestEmailFinder(unittest.TestCase):

    def test_find_email(self):
        text_with_email = "hfhhg test@gmail.com"
        self.assertEqual(app.find_email(text_with_email), "test@gmail.com")
        
    def test_email_not_found(self):
        text_without_email = "gfdfsf"
        with self.assertRaises(app.Exception):
            app.find_email(text_without_email)

if __name__ == '__main__':
    unittest.main()