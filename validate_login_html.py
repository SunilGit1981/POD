import unittest
from bs4 import BeautifulSoup
import os

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        with open('login.html', 'r') as file:
            self.html = file.read()

    def test_login_page_structure(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        self.assertIsNotNone(soup.find('div', class_='login-container'))
        self.assertIsNotNone(soup.find('div', class_='login-header'))
        self.assertIsNotNone(soup.find('form', class_='login-form'))
        self.assertIsNotNone(soup.find('input', id='userid'))
        self.assertIsNotNone(soup.find('input', id='password'))
        self.assertIsNotNone(soup.find('button', class_='login-button'))

    def test_login_form(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        form = soup.find('form', class_='login-form')
        self.assertIsNotNone(form)
        self.assertEqual(form.get('id'), 'login-form')

    def test_login_form_fields(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        form = soup.find('form', class_='login-form')
        self.assertIsNotNone(form.find('input', id='userid'))
        self.assertIsNotNone(form.find('input', id='password'))
        self.assertIsNotNone(form.find('button', class_='login-button'))

    def test_login_button(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        button = soup.find('button', class_='login-button')
        self.assertIsNotNone(button)
        self.assertEqual(button.get('type'), 'submit')

    def test_script_tag(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        script = soup.find('script')
        self.assertIsNotNone(script)

if __name__ == '__main__':
    unittest.main()