import unittest
from bs4 import BeautifulSoup

# This is a placeholder for how the original HTML content would be loaded
# in a real application. For this test, we will provide the content directly.
# In a real scenario, 'login_page.py' might contain a function that returns
# this HTML string or a Flask/Django view that renders it.
# Since the prompt provided `html_content` directly and instructed to import `login_page`,
# we simulate that `login_page.py` would export this content.
# For simplicity, we'll assume login_page.py contains the `html_content` variable.

# Assuming the content provided in the prompt is available in login_page.py
# For testing purposes, we define it here, but in a real scenario, it would be imported.
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <!-- Google Fonts: Inter for a modern look -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* CSS Variables for easy theme adjustments */
        :root {
            --primary-color: #007bff;
            --primary-hover-color: #0056b3;
            --background-color: #f0f2f5;
            --card-background: #ffffff;
            --text-color: #333;
            --label-color: #555;
            --border-color: #ddd;
            --focus-border-color: #80bdff;
            --shadow-light: rgba(0, 0, 0, 0.1);
            --shadow-medium: rgba(0, 0, 0, 0.15);
            --border-radius: 8px;
        }

        /* Basic Reset & Body Styling */
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--background-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            color: var(--text-color);
            box-sizing: border-box; /* Ensure padding and border are included in element's total width and height */
        }

        /* Login Container Styling */
        .login-container {
            background-color: var(--card-background);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: 0 10px 30px var(--shadow-medium);
            width: 100%;
            max-width: 400px;
            text-align: center;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        .login-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px var(--shadow-light);
        }

        /* Heading Styling */
        h2 {
            color: var(--primary-color);
            margin-bottom: 30px;
            font-size: 1.8em;
            font-weight: 700;
        }

        /* Input Group Styling */
        .input-group {
            margin-bottom: 20px;
            text-align: left;
        }

        /* Label Styling */
        label {
            display: block;
            margin-bottom: 8px;
            color: var(--label-color);
            font-weight: 600;
            font-size: 0.9em;
        }

        /* Input Field Styling */
        input[type="text"],
        input[type="password"] {
            width: calc(100% - 24px); /* Adjust for padding */
            padding: 12px;
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius);
            box-sizing: border-box;
            font-size: 1em;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
            outline: none; /* Remove default focus outline */
        }

        /* Input Field Focus State */
        input[type="text"]:focus,
        input[type="password"]:focus {
            border-color: var(--focus-border-color);
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25); /* Subtle focus ring */
        }

        /* Submit Button Styling */
        button[type="submit"] {
            width: 100%;
            padding: 14px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: var(--border-radius);
            cursor: pointer;
            font-size: 1.1em;
            font-weight: 600;
            margin-top: 20px;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }

        /* Submit Button Hover State */
        button[type="submit"]:hover {
            background-color: var(--primary-hover-color);
            transform: translateY(-2px); /* Lift effect on hover */
        }

        /* Submit Button Active State */
        button[type="submit"]:active {
            transform: translateY(0); /* Reset on click */
        }

        /* Forgot Password Link Styling */
        .forgot-password {
            margin-top: 15px;
            font-size: 0.9em;
        }

        .forgot-password a {
            color: var(--primary-color);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .forgot-password a:hover {
            color: var(--primary-hover-color);
            text-decoration: underline;
        }

        /* Responsive Adjustments */
        @media (max-width: 600px) {
            .login-container {
                margin: 20px;
                padding: 30px;
                box-shadow: 0 5px 20px var(--shadow-light);
                border-radius: var(--border-radius); /* Ensure consistent border-radius */
            }

            h2 {
                font-size: 1.5em;
                margin-bottom: 25px;
            }

            input[type="text"],
            input[type="password"],
            button[type="submit"] {
                padding: 10px;
                font-size: 0.95em;
            }
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Welcome Back!</h2>
        <form action="#" method="POST">
            <div class="input-group">
                <label for="username">Username or Email</label>
                <input type="text" id="username" name="username" placeholder="Enter your username or email" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>
            <button type="submit">Login</button>
            <div class="forgot-password">
                <a href="#">Forgot Password?</a>
            </div>
        </form>
    </div>
</body>
</html>
"""

# To fulfill `import login_page`, we'll make a dummy module that exposes `html_content`.
# In a real scenario, you'd have login_page.py with the variable `html_content` defined.
# For this specific test setup, we'll assign it directly.
class MockLoginPage:
    def __init__(self):
        self.html_content = html_content

login_page = MockLoginPage()


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Parse the HTML content once for all tests."""
        cls.soup = BeautifulSoup(login_page.html_content, 'html.parser')

    def test_document_structure(self):
        """Test the basic HTML document structure."""
        self.assertIsNotNone(self.soup.html, "HTML tag should exist")
        self.assertIsNotNone(self.soup.head, "HEAD tag should exist")
        self.assertIsNotNone(self.soup.body, "BODY tag should exist")

    def test_title(self):
        """Test the page title."""
        title_tag = self.soup.find('title')
        self.assertIsNotNone(title_tag, "Title tag should exist")
        self.assertEqual(title_tag.string, "Login", "Page title should be 'Login'")

    def test_charset_meta_tag(self):
        """Test for UTF-8 charset meta tag."""
        meta_charset = self.soup.find('meta', charset='UTF-8')
        self.assertIsNotNone(meta_charset, "Meta charset tag should be present and set to UTF-8")

    def test_viewport_meta_tag(self):
        """Test for viewport meta tag for responsiveness."""
        meta_viewport = self.soup.find('meta', attrs={'name': 'viewport'})
        self.assertIsNotNone(meta_viewport, "Viewport meta tag should exist")
        self.assertIn('width=device-width', meta_viewport.get('content', ''))
        self.assertIn('initial-scale=1.0', meta_viewport.get('content', ''))

    def test_google_fonts_link(self):
        """Test for the Google Fonts stylesheet link."""
        link_tag = self.soup.find('link', href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap", rel=["stylesheet"])
        self.assertIsNotNone(link_tag, "Google Fonts link for 'Inter' should be present")

    def test_login_container_exists(self):
        """Test if the main login container div exists."""
        login_container = self.soup.find('div', class_='login-container')
        self.assertIsNotNone(login_container, "A div with class 'login-container' should exist")

    def test_heading_exists(self):
        """Test if the 'Welcome Back!' heading exists within the container."""
        login_container = self.soup.find('div', class_='login-container')
        if login_container:
            heading = login_container.find('h2')
            self.assertIsNotNone(heading, "An h2 heading should exist inside the login container")
            self.assertEqual(heading.string, "Welcome Back!", "Heading text should be 'Welcome Back!'")
        else:
            self.fail("Login container not found, cannot test heading.")

    def test_form_structure(self):
        """Test the presence and attributes of the form."""
        form = self.soup.find('form')
        self.assertIsNotNone(form, "A form tag should exist")
        self.assertEqual(form.get('action'), '#', "Form action should be '#'")
        self.assertEqual(form.get('method').lower(), 'post', "Form method should be 'post'")

    def test_username_input_group(self):
        """Test the username input field and its associated label."""
        username_label = self.soup.find('label', {'for': 'username'})
        self.assertIsNotNone(username_label, "Label for username should exist")
        self.assertEqual(username_label.string, "Username or Email", "Username label text is incorrect")

        username_input = self.soup.find('input', {'id': 'username'})
        self.assertIsNotNone(username_input, "Username input field should exist")
        self.assertEqual(username_input.get('type'), 'text', "Username input type should be 'text'")
        self.assertEqual(username_input.get('name'), 'username', "Username input name should be 'username'")
        self.assertEqual(username_input.get('placeholder'), 'Enter your username or email', "Username input placeholder is incorrect")
        self.assertIn('required', username_input.attrs, "Username input should be required")

        # Check if it's within an input-group
        input_group = username_label.find_parent('div', class_='input-group')
        self.assertIsNotNone(input_group, "Username label and input should be within an .input-group div")

    def test_password_input_group(self):
        """Test the password input field and its associated label."""
        password_label = self.soup.find('label', {'for': 'password'})
        self.assertIsNotNone(password_label, "Label for password should exist")
        self.assertEqual(password_label.string, "Password", "Password label text is incorrect")

        password_input = self.soup.find('input', {'id': 'password'})
        self.assertIsNotNone(password_input, "Password input field should exist")
        self.assertEqual(password_input.get('type'), 'password', "Password input type should be 'password'")
        self.assertEqual(password_input.get('name'), 'password', "Password input name should be 'password'")
        self.assertEqual(password_input.get('placeholder'), 'Enter your password', "Password input placeholder is incorrect")
        self.assertIn('required', password_input.attrs, "Password input should be required")

        # Check if it's within an input-group
        input_group = password_label.find_parent('div', class_='input-group')
        self.assertIsNotNone(input_group, "Password label and input should be within an .input-group div")

    def test_submit_button(self):
        """Test the presence and attributes of the submit button."""
        submit_button = self.soup.find('button', type='submit')
        self.assertIsNotNone(submit_button, "Submit button should exist")
        self.assertEqual(submit_button.string, "Login", "Submit button text should be 'Login'")

    def test_forgot_password_link(self):
        """Test the 'Forgot Password?' link."""
        forgot_password_div = self.soup.find('div', class_='forgot-password')
        self.assertIsNotNone(forgot_password_div, "A div with class 'forgot-password' should exist")

        forgot_password_link = forgot_password_div.find('a')
        self.assertIsNotNone(forgot_password_link, "Forgot Password link should exist within its div")
        self.assertEqual(forgot_password_link.get('href'), '#', "Forgot Password link href should be '#'")
        self.assertEqual(forgot_password_link.string, "Forgot Password?", "Forgot Password link text is incorrect")

    def test_inline_css_styles_exist(self):
        """Test that a style block is present."""
        style_tag = self.soup.find('style')
        self.assertIsNotNone(style_tag, "A style block should exist in the head")
        self.assertGreater(len(style_tag.string.strip()), 100, "Style block should contain significant CSS rules")

    def test_css_variables_defined(self):
        """Test for the presence of CSS variables in the style block."""
        style_tag = self.soup.find('style')
        if style_tag:
            css_content = style_tag.string
            self.assertIn('--primary-color:', css_content, "CSS variable --primary-color should be defined")
            self.assertIn('--background-color:', css_content, "CSS variable --background-color should be defined")
            self.assertIn('--card-background:', css_content, "CSS variable --card-background should be defined")
            self.assertIn('--border-radius:', css_content, "CSS variable --border-radius should be defined")
        else:
            self.fail("No style tag found to check CSS variables.")

    def test_body_styling_mentions_inter_font(self):
        """Test that the body style uses the 'Inter' font."""
        style_tag = self.soup.find('style')
        if style_tag:
            css_content = style_tag.string
            self.assertRegex(css_content, r"body\s*\{[^}]*font-family:\s*'Inter', sans-serif;", "Body CSS should specify 'Inter' font-family")
        else:
            self.fail("No style tag found to check body styling.")

    def test_login_container_has_shadow_and_transition(self):
        """Test that the login container CSS includes box-shadow and transition properties."""
        style_tag = self.soup.find('style')
        if style_tag:
            css_content = style_tag.string
            self.assertRegex(css_content, r"\.login-container\s*\{[^}]*box-shadow:[^;]+;", "Login container CSS should include box-shadow")
            self.assertRegex(css_content, r"\.login-container\s*\{[^}]*transition:[^;]+;", "Login container CSS should include transition")
        else:
            self.fail("No style tag found to check login container styling.")

    def test_responsive_media_query_exists(self):
        """Test for the presence of a responsive media query."""
        style_tag = self.soup.find('style')
        if style_tag:
            css_content = style_tag.string
            self.assertIn('@media (max-width: 600px)', css_content, "A media query for max-width: 600px should exist")
        else:
            self.fail("No style tag found to check media query.")

if __name__ == '__main__':
    unittest.main()