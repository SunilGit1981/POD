import unittest
import re

class TestIndexHtml(unittest.TestCase):

    def setUp(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            self.content = file.read()

    def test_header_exists(self):
        self.assertTrue('<header' in self.content.lower())

    def test_main_exists(self):
        self.assertTrue('<main' in self.content.lower())

    def test_footer_exists(self):
        self.assertTrue('<footer' in self.content.lower())

    def test_login_form_exists(self):
        self.assertTrue('<div class="login-form"' in self.content.lower())

    def test_input_fields_exist(self):
        self.assertTrue('<input type="text"' in self.content.lower())
        self.assertTrue('<input type="password"' in self.content.lower())

    def test_buttons_exist(self):
        self.assertTrue('<button type="button"' in self.content.lower())
        self.assertTrue('<button class="google-btn"' in self.content.lower())
        self.assertTrue('<button class="gmail-btn"' in self.content.lower())

    def test_input_field_width(self):
        input_fields = re.findall(r'<input[^>]*style="[^"]*width:[^;"]*"', self.content)
        for field in input_fields:
            self.assertTrue('width: 100%' in field)

    def test_button_width(self):
        buttons = re.findall(r'<button[^>]*style="[^"]*width:[^;"]*"', self.content)
        for button in buttons:
            self.assertTrue('width: 100%' in button)

    def test_no_overlapping(self):
        # Check if there are any overlapping elements
        # This is a basic check and may not cover all cases
        self.assertFalse('position: absolute' in self.content)

if __name__ == '__main__':
    unittest.main()