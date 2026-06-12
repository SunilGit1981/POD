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

print(html_content)