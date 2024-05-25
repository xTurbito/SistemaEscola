from flask import render_template

def login():
    return render_template('views/auth/login.html')