import unittest
import re # To assist with more robust HTML parsing if needed, but string checks are sufficient here

# Assume the generate_login_page_html function is in a file named `html_generator.py`
# or similar, for demonstration purposes.
# For the purpose of providing raw test code, I will include the function definition here
# as if it were imported, or assume it's available in the same scope.
# If this code were in a separate file (e.g., `math_utils.py` as per instruction),
# it would be `from math_utils import generate_login_page_html`.

# Code to test (copied here for self-contained test execution, but in practice,
# it would be imported from `math_utils.py` or similar).
def generate_login_page_html(message=""):
    """
    Generates a modern HTML login page with optional message display.
    """
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
            color: #333;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}
        .login-container {{
            background-color: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
            box-sizing: border-box; /* Include padding in width */
        }}
        .login-container h2 {{
            margin-bottom: 30px;
            color: #333;
            font-weight: 500;
            font-size: 1.8em;
        }}
        .form-group {{
            margin-bottom: 20px;
            text-align: left;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 8px;
            font-weight: 400;
            color: #555;
            font-size: 0.95em;
        }}
        .form-group input[type="text"],
        .form-group input[type="password"] {{
            width: 100%;
            padding: 12px 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
            box-sizing: border-box; /* Include padding and border in width */
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }}
        .form-group input[type="text"]:focus,
        .form-group input[type="password"]:focus {{
            border-color: #007bff;
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
            outline: none;
        }}
        .btn-primary {{
            background-color: #007bff;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1.1em;
            font-weight: 500;
            transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
            width: 100%;
            margin-top: 10px;
        }}
        .btn-primary:hover {{
            background-color: #0056b3;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 123, 255, 0.3);
        }}
        .btn-primary:active {{
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }}
        .message {{
            margin-top: 20px;
            padding: 12px;
            border-radius: 8px;
            font-size: 0.9em;
            text-align: center;
            opacity: { "1" if message else "0" };
            max-height: { "100px" if message else "0px" };
            overflow: hidden;
            transition: opacity 0.3s ease-in-out, max-height 0.3s ease-in-out;
            margin-bottom: { "20px" if message else "0" };
        }}
        .message.error {{
            color: #d63300; /* Error red */
            background-color: #ffebe8; /* Light error background */
            border: 1px solid #ffc2b3;
        }}
        .message.success {{
            color: #155724; /* Success green */
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
        }}
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Welcome Back!</h2>
        <form action="/login" method="post">
            {f'<div class="message error">{message}</div>' if message else ''}
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>
            <button type="submit" class="btn-primary">Login</button>
        </form>
    </div>
</body>
</html>
    """
    return html_content


class TestLoginPageGenerator(unittest.TestCase):

    def test_generate_login_page_no_message(self):
        """
        Tests the generation of the login page HTML when no message is provided.
        Ensures the message div is absent and CSS properties reflect no message.
        """
        html = generate_login_page_html()

        # Check for essential HTML structure elements
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn('<html lang="en">', html)
        self.assertIn("<head>", html)
        self.assertIn("<body>", html)
        self.assertIn("<title>Login</title>", html)
        self.assertIn("<h2>Welcome Back!</h2>", html)
        self.assertIn('<form action="/login" method="post">', html)
        self.assertIn('<input type="text" id="username" name="username"', html)
        self.assertIn('<input type="password" id="password" name="password"', html)
        self.assertIn('<button type="submit" class="btn-primary">Login</button>', html)

        # Ensure no message div is present
        self.assertNotIn('<div class="message error">', html)
        self.assertNotIn('message error', html) # Double check to avoid partial matches

        # Check CSS for message visibility when no message
        self.assertIn("opacity: 0;", html, "CSS opacity should be 0 for no message")
        self.assertIn("max-height: 0px;", html, "CSS max-height should be 0px for no message")
        self.assertIn("margin-bottom: 0;", html, "CSS margin-bottom should be 0 for no message")

    def test_generate_login_page_with_message(self):
        """
        Tests the generation of the login page HTML when a message is provided.
        Ensures the message div is present with correct content and class,
        and CSS properties reflect message visibility.
        """
        test_message = "Invalid username or password!"
        html = generate_login_page_html(message=test_message)

        # Check for essential HTML structure elements (re-verify basic functionality)
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("<title>Login</title>", html)
        self.assertIn("<h2>Welcome Back!</h2>", html)
        self.assertIn('<input type="text" id="username"', html)
        self.assertIn('<button type="submit" class="btn-primary">Login</button>', html)

        # Ensure the message div is present with the correct content and class
        expected_message_div = f'<div class="message error">{test_message}</div>'
        self.assertIn(expected_message_div, html, "The message div should contain the provided message and error class")

        # Check CSS for message visibility when a message is present
        self.assertIn("opacity: 1;", html, "CSS opacity should be 1 when a message is present")
        self.assertIn("max-height: 100px;", html, "CSS max-height should be 100px when a message is present")
        self.assertIn("margin-bottom: 20px;", html, "CSS margin-bottom should be 20px when a message is present")

        # Verify specific error message styling
        self.assertIn("color: #d63300;", html, "Error message should have specific red color")
        self.assertIn("background-color: #ffebe8;", html, "Error message should have specific light error background")

    def test_html_head_content(self):
        """
        Tests the content within the <head> section of the generated HTML.
        """
        html = generate_login_page_html()
        self.assertIn('<meta charset="UTF-8">', html)
        self.assertIn('<meta name="viewport" content="width=device-width, initial-scale=1.0">', html)
        self.assertIn('<title>Login</title>', html)
        self.assertIn('<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">', html)

    def test_html_form_elements_attributes(self):
        """
        Tests the presence and attributes of key form elements.
        """
        html = generate_login_page_html()

        # Form tag attributes
        self.assertIn('<form action="/login" method="post">', html)

        # Username input field
        self.assertIn('<label for="username">Username</label>', html)
        self.assertIn('<input type="text" id="username" name="username" placeholder="Enter your username" required>', html)

        # Password input field
        self.assertIn('<label for="password">Password</label>', html)
        self.assertIn('<input type="password" id="password" name="password" placeholder="Enter your password" required>', html)

        # Submit button
        self.assertIn('<button type="submit" class="btn-primary">Login</button>', html)

    def test_css_base_styling_elements(self):
        """
        Tests for the presence of specific CSS classes and properties,
        ensuring basic styling is included.
        """
        html = generate_login_page_html()
        self.assertIn("font-family: 'Roboto', sans-serif;", html)
        self.assertIn(".login-container", html)
        self.assertIn(".form-group", html)
        self.assertIn(".btn-primary", html)
        self.assertIn("background-color: #f0f2f5;", html) # body background
        self.assertIn("box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);", html) # container shadow
        self.assertIn("background-color: #007bff;", html) # primary button color

    def test_message_with_special_characters_html_injection(self):
        """
        Tests if a message with special HTML characters is rendered directly.
        (Note: The current implementation does not sanitize HTML, it injects directly).
        """
        malicious_message = "<b>Warning!</b> <script>alert('XSS');</script>"
        html = generate_login_page_html(message=malicious_message)
        self.assertIn(f'<div class="message error">{malicious_message}</div>', html)
        self.assertIn("<b>Warning!</b>", html)
        self.assertIn("<script>alert('XSS');</script>", html)


if __name__ == '__main__':
    unittest.main()