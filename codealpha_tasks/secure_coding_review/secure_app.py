from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
app.secret_key = '1234567890abcdef'

users = {
    'admin': 'admin123'
}

@app.route('/')
def index():
    return '''
        <h2>Login</h2>
        <form method="post" action="/login">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        safe_username = escape(username)
        return f"Welcome, {safe_username}!"
    else:
        return "Invalid credentials."

if __name__ == '__main__':
    app.run(debug=True)
