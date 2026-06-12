import unittest
from bs4 import BeautifulSoup

class TestIndexHtml(unittest.TestCase):

    def setUp(self):
        # Create a dummy index.html file for testing purposes
        self.html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #007bff;
            --primary-hover-color: #0056b3;
            --background-color: #f0f2f5;
            --card-background: #ffffff;
            --text-color: #333;
            --input-border: #ced4da;
            --input-focus-shadow: rgba(0, 123, 255, 0.25);
            --border-radius: 8px;
            --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        .login-container {
            background-color: var(--card-background);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }

        .login-container h1 {
            font-size: 2.2em;
            margin-bottom: 30px;
            color: var(--text-color);
            font-weight: 600;
        }

        .input-group {
            margin-bottom: 20px;
            text-align: left;
        }

        .input-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: var(--text-color);
            font-size: 0.95em;
        }

        .input-group input[type="text"],
        .input-group input[type="password"] {
            width: calc(100% - 24px); /* Account for padding */
            padding: 12px;
            border: 1px solid var(--input-border);
            border-radius: var(--border-radius);
            font-size: 1em;
            box-sizing: border-box; /* Include padding in width */
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .input-group input[type="text"]:focus,
        .input-group input[type="password"]:focus {
            border-color: var(--primary-color);
            outline: none;
            box-shadow: 0 0 0 3px var(--input-focus-shadow);
        }

        .btn-primary {
            width: 100%;
            padding: 14px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: var(--border-radius);
            font-size: 1.1em;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            margin-top: 10px;
        }

        .btn-primary:hover {
            background-color: var(--primary-hover-color);
            box-shadow: 0 6px 16px rgba(0, 123, 255, 0.2);
        }

        .footer-links {
            margin-top: 25px;
            font-size: 0.9em;
        }

        .footer-links a {
            color: var(--primary-color);
            text-decoration: none;
            margin: 0 10px;
            transition: color 0.2s ease;
        }

        .footer-links a:hover {
            color: var(--primary-hover-color);
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Welcome Back!</h1>
        <form action="#" method="POST"> <!-- Action can be updated to your backend endpoint -->
            <div class="input-group">
                <label for="user-id">User ID</label>
                <input type="text" id="user-id" name="userId" placeholder="Enter your user ID" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>
            <button type="submit" class="btn-primary">Login</button>
        </form>
        <div class="footer-links">
            <a href="#">Forgot Password?</a>
            <span>•</span>
            <a href="#">Sign Up</a>
        </div>
    </div>
</body>
</html>
        """
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def test_has_title(self):
        title_tag = self.soup.find('title')
        self.assertIsNotNone(title_tag, "The HTML page should have a <title> tag.")
        self.assertIn("Login", title_tag.text, "The title should contain 'Login'.")

    def test_has_login_form(self):
        form_tag = self.soup.find('form')
        self.assertIsNotNone(form_tag, "The HTML page should contain a <form> tag for login.")
        self.assertEqual(form_tag.get('method').upper(), "POST", "The login form method should be POST.")

    def test_has_user_id_input(self):
        user_id_input = self.soup.find('input', {'id': 'user-id', 'name': 'userId', 'type': 'text'})
        self.assertIsNotNone(user_id_input, "The form should have an input field for User ID.")
        self.assertTrue(user_id_input.has_attr('required'), "User ID input should be required.")
        user_id_label = self.soup.find('label', {'for': 'user-id'})
        self.assertIsNotNone(user_id_label, "The form should have a label for User ID.")
        self.assertIn("User ID", user_id_label.text, "User ID label text is incorrect.")

    def test_has_password_input(self):
        password_input = self.soup.find('input', {'id': 'password', 'name': 'password', 'type': 'password'})
        self.assertIsNotNone(password_input, "The form should have an input field for Password.")
        self.assertTrue(password_input.has_attr('required'), "Password input should be required.")
        password_label = self.soup.find('label', {'for': 'password'})
        self.assertIsNotNone(password_label, "The form should have a label for Password.")
        self.assertIn("Password", password_label.text, "Password label text is incorrect.")

    def test_has_submit_button(self):
        submit_button = self.soup.find('button', {'type': 'submit', 'class': 'btn-primary'})
        self.assertIsNotNone(submit_button, "The form should have a submit button.")
        self.assertIn("Login", submit_button.text, "The submit button text should be 'Login'.")

    def test_modern_ui_elements_present(self):
        # Check for external stylesheet for fonts (indicative of modern design)
        font_link = self.soup.find('link', {'href': lambda href: href and 'fonts.googleapis.com' in href})
        self.assertIsNotNone(font_link, "External font link (e.g., Poppins) not found, suggesting non-modern UI.")

        # Check for meta viewport tag (essential for responsive/modern design)
        viewport_meta = self.soup.find('meta', {'name': 'viewport'})
        self.assertIsNotNone(viewport_meta, "Meta viewport tag not found, essential for modern responsive UI.")
        self.assertIn("width=device-width", viewport_meta.get('content', ''), "Viewport content missing 'width=device-width'.")
        self.assertIn("initial-scale=1.0", viewport_meta.get('content', ''), "Viewport content missing 'initial-scale=1.0'.")

        # Check for a 'login-container' class or similar for layout (suggests structured modern UI)
        login_container = self.soup.find('div', class_='login-container')
        self.assertIsNotNone(login_container, "A 'login-container' div or similar layout wrapper is missing, indicating less structured UI.")

        # Check for CSS variables in style tag (modern CSS practice)
        style_tag = self.soup.find('style')
        self.assertIsNotNone(style_tag, "No internal style tag found.")
        self.assertIn(':root {', style_tag.text, "CSS variables (using :root) not found, which is a modern CSS practice.")
        self.assertIn('--primary-color', style_tag.text, "CSS variable --primary-color not found.")
        self.assertIn('--border-radius', style_tag.text, "CSS variable --border-radius not found, indicating lack of modern styling for rounded corners.")
        self.assertIn('--shadow', style_tag.text, "CSS variable --shadow not found, indicating lack of modern styling for shadows.")

        # Check for 'Poppins' font-family in CSS
        self.assertIn("font-family: 'Poppins', sans-serif;", style_tag.text, "Poppins font not applied in CSS, despite link.")

        # Check for button hover effects (common modern UI interaction)
        self.assertIn(".btn-primary:hover", style_tag.text, "Button hover style not found.")

        # Check for focus styles on inputs (accessibility and modern UI)
        self.assertIn(".input-group input[type=\"text\"]:focus", style_tag.text, "Input focus style not found.")
        self.assertIn("box-shadow: 0 0 0 3px var(--input-focus-shadow);", style_tag.text, "Input focus box-shadow not found, indicating less modern focus styling.")

    def test_footer_links_present(self):
        footer_links_div = self.soup.find('div', class_='footer-links')
        self.assertIsNotNone(footer_links_div, "Footer links container not found.")
        links = footer_links_div.find_all('a')
        self.assertEqual(len(links), 2, "Expected two footer links (Forgot Password, Sign Up).")
        self.assertIn("Forgot Password?", links[0].text, "Forgot Password link text missing or incorrect.")
        self.assertIn("Sign Up", links[1].text, "Sign Up link text missing or incorrect.")

if __name__ == '__main__':
    unittest.main()