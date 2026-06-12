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

# Example usage:
if __name__ == "__main__":
    # To generate HTML with an error message:
    # login_page_with_error = generate_login_page_html(message="Invalid username or password.")
    # print(login_page_with_error)

    # To generate HTML without a message (default):
    login_page = generate_login_page_html()
    
    # Save the generated HTML to a file
    file_path = "login.html" # You can change this to any desired HTML file name
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(login_page)
    print(f"HTML login page generated successfully at: {file_path}")

    # You can also generate with a success message (requires styling adjustment for .success class)
    # success_page = generate_login_page_html(message="Login successful!")
    # with open("login_success.html", "w", encoding="utf-8") as f:
    #     f.write(success_page)
    # print("login_success.html generated.")