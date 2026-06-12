import unittest
from bs4 import BeautifulSoup
import os

class TestIndexHtml(unittest.TestCase):

    def setUp(self):
        with open('index.html', 'r') as file:
            self.html_content = file.read()

    def test_doctype_declaration(self):
        self.assertIn('<!DOCTYPE html>', self.html_content)

    def test_html_tag(self):
        self.assertIn('<html lang="en">', self.html_content)

    def test_head_tag(self):
        self.assertIn('<head>', self.html_content)

    def test_meta_tags(self):
        self.assertIn('<meta charset="UTF-8">', self.html_content)
        self.assertIn('<meta name="viewport" content="width=device-width, initial-scale=1.0">', self.html_content)

    def test_title_tag(self):
        self.assertIn('<title>Responsive Dark Theme</title>', self.html_content)

    def test_style_tag(self):
        self.assertIn('<style>', self.html_content)

    def test_body_tag(self):
        self.assertIn('<body>', self.html_content)

    def test_header_tag(self):
        self.assertIn('<header>', self.html_content)

    def test_main_tag(self):
        self.assertIn('<main>', self.html_content)

    def test_footer_tag(self):
        self.assertIn('<footer>', self.html_content)

    def test_copyright_statement(self):
        self.assertIn('&#169; 2024 Responsive Dark Theme. All rights reserved.', self.html_content)

    def test_responsive_css(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        style_tag = soup.find('style')
        self.assertIsNotNone(style_tag)
        self.assertIn('@media only screen and (max-width: 768px)', style_tag.text)

    def test_dark_layout(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        style_tag = soup.find('style')
        self.assertIsNotNone(style_tag)
        self.assertIn('background-color: #2f2f2f', style_tag.text)
        self.assertIn('color: #ffffff', style_tag.text)

if __name__ == '__main__':
    unittest.main()