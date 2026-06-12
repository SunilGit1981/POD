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
        self.assertIn('</head>', self.html)

    def test_title_tag(self):
        self.assertIn('<title>Login Page</title>', self.html)

    def test_style_tag(self):
        self.assertIn('<style>', self.html)
        self.assertIn('</style>', self.html)

    def test_body_tag(self):
        self.assertIn('<body>', self.html)
        self.assertIn('</body>', self.html)

    def test_container_div(self):
        self.assertIn('<div class="container">', self.html)
        self.assertIn('</div>', self.html)

    def test_form_tag(self):
        self.assertIn('<form>', self.html)
        self.assertIn('</form>', self.html)

    def test_form_group_div(self):
        self.assertIn('<div class="form-group">', self.html)
        self.assertIn('</div>', self.html)

    def test_label_tags(self):
        self.assertIn('<label for="userid">User ID:</label>', self.html)
        self.assertIn('<label for="password">Password:</label>', self.html)

    def test_input_tags(self):
        self.assertIn('<input type="text" id="userid" name="userid" required>', self.html)
        self.assertIn('<input type="password" id="password" name="password" required>', self.html)

    def test_button_tag(self):
        self.assertIn('<button class="btn" type="submit">Login</button>', self.html)

    def test_footer_tag(self):
        self.assertIn('<footer>', self.html)
        self.assertIn('</footer>', self.html)

    def test_copyright_statement(self):
        self.assertIn('&copy; 2024 Login Page. All rights reserved.', self.html)

    def test_responsive_css(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        self.assertIn('max-width: 300px', soup.find('style').text)
        self.assertIn('margin: 40px auto', soup.find('style').text)
        self.assertIn('padding: 20px', soup.find('style').text)
        self.assertIn('background-color: #4f4f4f', soup.find('style').text)
        self.assertIn('border-radius: 10px', soup.find('style').text)
        self.assertIn('box-shadow: 0 0 10px rgba(0, 0, 0, 0.2)', soup.find('style').text)

    def test_dark_layout(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        self.assertIn('background-color: #2f2f2f', soup.find('style').text)
        self.assertIn('color: #ffffff', soup.find('style').text)

if __name__ == '__main__':
    unittest.main()