import unittest
from bs4 import BeautifulSoup
import os

class TestIndexHtml(unittest.TestCase):

    def setUp(self):
        with open('index.html', 'r') as file:
            self.html_content = file.read()

    def test_html_structure(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        self.assertIsNotNone(soup.find('header'))
        self.assertIsNotNone(soup.find('main'))
        self.assertIsNotNone(soup.find('footer'))

    def test_login_form(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        login_form = soup.find('div', class_='login-form')
        self.assertIsNotNone(login_form)
        self.assertIsNotNone(login_form.find('input', id='user-id'))
        self.assertIsNotNone(login_form.find('input', id='password'))
        self.assertIsNotNone(login_form.find('button', type='button'))

    def test_input_fields(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        user_id_input = soup.find('input', id='user-id')
        password_input = soup.find('input', id='password')
        self.assertEqual(user_id_input['type'], 'text')
        self.assertEqual(password_input['type'], 'password')

    def test_button(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        button = soup.find('button', type='button')
        self.assertEqual(button['type'], 'button')
        self.assertEqual(button.text, 'Login')

if __name__ == '__main__':
    unittest.main()