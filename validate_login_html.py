import unittest
from bs4 import BeautifulSoup
import os

class TestLoginHtml(unittest.TestCase):

    def setUp(self):
        with open('login.html', 'r') as file:
            self.html = file.read()

    def test_doctype(self):
        self.assertIn('<!DOCTYPE html>', self.html)

    def test_html_tag(self):
        self.assertIn('<html lang="en">', self.html)

    def test_head_tag(self):
        self.assertIn('<head>', self.html)

    def test_title_tag(self):
        self.assertIn('<title>Login Page</title>', self.html)

    def test_style_tag(self):
        self.assertIn('<style>', self.html)

    def test_body_tag(self):
        self.assertIn('<body>', self.html)

    def test_container_div(self):
        self.assertIn('<div class="container">', self.html)

    def test_form_tag(self):
        self.assertIn('<form>', self.html)

    def test_userid_input(self):
        self.assertIn('<input type="text" id="userid" name="userid" required>', self.html)

    def test_password_input(self):
        self.assertIn('<input type="password" id="password" name="password" required>', self.html)

    def test_login_button(self):
        self.assertIn('<button class="btn" type="submit">Login</button>', self.html)

    def test_footer_tag(self):
        self.assertIn('<footer>', self.html)

    def test_copyright_statement(self):
        self.assertIn('&copy; 2024 Login Page. All rights reserved.', self.html)

    def test_responsive_css(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        self.assertIsNotNone(soup.find('meta', attrs={'name': 'viewport'}))

    def test_dark_layout(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        style_tag = soup.find('style')
        self.assertIsNotNone(style_tag)
        self.assertIn('background-color: #2f2f2f', str(style_tag))

if __name__ == '__main__':
    unittest.main()