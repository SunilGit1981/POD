import unittest
import os

class TestIndexHtml(unittest.TestCase):

    def test_index_html_exists(self):
        self.assertTrue(os.path.exists('index.html'))

    def test_index_html_content(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertTrue('<header' in content.lower())
            self.assertTrue('<main' in content.lower())
            self.assertTrue('<footer' in content.lower())
            self.assertTrue('<div class="login-form"' in content.lower())
            self.assertTrue('<button class="google-btn"' in content.lower())
            self.assertTrue('<button class="gmail-btn"' in content.lower())
            self.assertTrue('handleCredentialResponse' in content)
            self.assertTrue('handleGmailAuthentication' in content)
            self.assertTrue('google.accounts.id.initialize' in content)
            self.assertTrue('google.accounts.id.renderButton' in content)

    def test_gmail_authentication(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertTrue('handleGmailAuthentication' in content)
            self.assertTrue('window.location.href = \'https://accounts.google.com/o/oauth2/auth?' in content)

    def test_google_signin(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertTrue('google.accounts.id.initialize' in content)
            self.assertTrue('google.accounts.id.renderButton' in content)

if __name__ == '__main__':
    unittest.main()