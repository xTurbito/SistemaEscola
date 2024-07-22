# app/controllers/licenciaturas_controller.py

from flask import Blueprint
from app.models.database import get_db_connection
from app.views.licenciaturas_views import render_licenciaturas_index, render_add_licenciatura

licenciaturas_bp = Blueprint('licenciaturas', __name__, url_prefix='/licenciaturas')

@licenciaturas_bp.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM licenciaturas')
    licenciaturas_data = cur.fetchall()
    cur.close()
    conn.close()
    return render_licenciaturas_index(licenciaturas_data)

@licenciaturas_bp.route('/add', methods=['GET'])
def add():
    return render_add_licenciatura()
