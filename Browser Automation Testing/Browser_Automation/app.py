
from flask import Flask, request, render_template_string

app = Flask(__name__)

users = {}

html = """
<h2>Registration Page</h2>

<form method="POST" action="/register">
    <input name="username" placeholder="Enter Username" required>
    <br><br>

    <input name="email" placeholder="Enter Email" required>
    <br><br>

    <input name="password" type="password"
           placeholder="Enter Password" required>
    <br><br>

    <button type="submit">Register</button>
</form>

<h2>Login Page</h2>

<form method="POST" action="/login">
    <input name="username" placeholder="Enter Username" required>
    <br><br>

    <input name="password" type="password"
           placeholder="Enter Password" required>
    <br><br>

    <button type="submit">Login</button>
</form>

<p>{{ message }}</p>
"""

@app.route("/")
def home():
    return render_template_string(html, message="")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    users[username] = {
        "email": email,
        "password": password
    }

    return render_template_string(
        html,
        message="Registration Successful"
    )

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username]["password"] == password:
        message = "Login Successful"
    else:
        message = "Invalid Username or Password"

    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run(debug=True)
