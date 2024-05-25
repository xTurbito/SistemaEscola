from flask import Flask
from flask import render_template
from Controllers import UsuarioController

app = Flask(__name__)

@app.route('/')
def login():
    return UsuarioController.login()

@app.route('/panel')
def panel():
    return render_template('views/panel/index.html')