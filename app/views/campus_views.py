# app/views/campus_views.py

from flask import render_template

def render_campus_index(campus_data):
    return render_template('panel/campus/index.html', campus=campus_data)

def render_edit_campus(campus_data):
    return render_template('panel/campus/edit_campus.html', campus=campus_data)

def render_add_campus():
    return render_template('panel/campus/add_campus.html')
