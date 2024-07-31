from flask import Blueprint, request, redirect, url_for, session, flash
from app.models.database import get_db_connection
from app.views.campus_views import render_campus_index, render_edit_campus, render_add_campus

campus_bp = Blueprint('campus', __name__, url_prefix='/campus')

@campus_bp.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM campus')
    campus_data = cur.fetchall()
    cur.close()
    conn.close()
    return render_campus_index(campus_data)

@campus_bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM campus WHERE idCampus = %s', (id,))
    campus_data = cur.fetchone()
    cur.close()
    conn.close()
    return render_edit_campus(campus_data)

@campus_bp.route('/add', methods=['GET'])
def add():
    return render_add_campus()
    