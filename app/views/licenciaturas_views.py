# app/views/licenciaturas_views.py

from flask import render_template

def render_licenciaturas_index(licenciaturas_data):
    return render_template('panel/licenciaturas/index.html', licenciaturas=licenciaturas_data)

def render_add_licenciatura():
    return render_template('panel/licenciaturas/add_licenciatura.html')
