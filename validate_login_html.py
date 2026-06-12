import unittest
from bs4 import BeautifulSoup

class TestLoginHtml(unittest.TestCase):

    def setUp(self):
        with open('login.html', 'r') as file:
            self.html_content = file.read()
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def test_gmail_auth_button(self):
        gmail_auth_button = self.soup.find('button', id='gmail-auth-button')
        self.assertIsNotNone(gmail_auth_button)
        self.assertEqual(gmail_auth_button.text, 'Sign in with Gmail')

    def test_gmail_auth_script(self):
        script_tags = self.soup.find_all('script')
        gmail_auth_script = None
        for script in script_tags:
            if 'gmailAuthButton' in str(script):
                gmail_auth_script = script
                break
        self.assertIsNotNone(gmail_auth_script)

    def test_gmail_auth_container(self):
        gmail_auth_container = self.soup.find('div', id='gmail-auth-container')
        self.assertIsNotNone(gmail_auth_container)

    def test_gmail_auth_script_content(self):
        script_tags = self.soup.find_all('script')
        gmail_auth_script = None
        for script in script_tags:
            if 'gmailAuthButton' in str(script):
                gmail_auth_script = script
                break
        self.assertIsNotNone(gmail_auth_script)
        self.assertIn('https://accounts.google.com/o/oauth2/v2/auth', str(gmail_auth_script))
        self.assertIn('https://openidconnect.googleapis.com/v1/userinfo', str(gmail_auth_script))

if __name__ == '__main__':
    unittest.main()