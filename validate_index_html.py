import unittest
from html.parser import HTMLParser

class TestIndexHtml(unittest.TestCase):
    def setUp(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            self.html_content = file.read()

    def test_header(self):
        self.assertIn('<header>', self.html_content)
        self.assertIn('<h1>Responsive Theme</h1>', self.html_content)
        self.assertIn('</header>', self.html_content)

    def test_footer(self):
        self.assertIn('<footer>', self.html_content)
        self.assertIn('&#169; 2024 Responsive Theme. All rights reserved.', self.html_content)
        self.assertIn('</footer>', self.html_content)

    def test_login_form(self):
        self.assertIn('<div class="login-form">', self.html_content)
        self.assertIn('<input type="text" id="user-id" placeholder="User ID">', self.html_content)
        self.assertIn('<input type="password" id="password" placeholder="Password">', self.html_content)
        self.assertIn('<button type="button" id="login-btn">Login</button>', self.html_content)
        self.assertIn('<button class="gmail-btn" id="gmail-signin-btn">Sign in with Gmail</button>', self.html_content)

    def test_landing_page(self):
        self.assertIn('<main class="landing-page" id="landing-page">', self.html_content)
        self.assertIn('<div class="landing-page-container">', self.html_content)
        self.assertIn('<div class="left-nav">', self.html_content)
        self.assertIn('<div class="main-content">', self.html_content)

    def test_script_tags(self):
        self.assertIn('<script>', self.html_content)
        self.assertIn('function handleGmailAuthentication()', self.html_content)
        self.assertIn('window.onload = function () {', self.html_content)
        self.assertIn('</script>', self.html_content)

    def test_style_tags(self):
        self.assertIn('<style>', self.html_content)
        self.assertIn('body {', self.html_content)
        self.assertIn('header {', self.html_content)
        self.assertIn('main {', self.html_content)
        self.assertIn('footer {', self.html_content)
        self.assertIn('</style>', self.html_content)

if __name__ == '__main__':
    unittest.main()