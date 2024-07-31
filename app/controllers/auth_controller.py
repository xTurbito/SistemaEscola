from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.database import get_db_connection

auth_bp = Blueprint('auth', __name__, url_prefix='/')

@auth_bp.route('/')
def index():
    if session.get('logged_in'):
        return render_template('auth/login.html') 
    return render_template('auth/login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        cCorreo = request.form['correo']
        cPassword = request.form['password']
        
        # Conectar a la base de datos
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT idUsuario FROM usuarios WHERE cCorreo = %s AND cPassword = %s', (cCorreo, cPassword))
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user:
            idUsuario = user[0]
            session['logged_in'] = True
            session['idUsuario'] = idUsuario
            return redirect(url_for('panel.index'))  # Cambia 'campus.index' según el controlador y la vista a la que quieras redirigir
        else:
            flash('Login fallido. Verifica tu usuario y contraseña', 'error')
            return redirect(url_for('auth.index'))  # Redirige a la página de login si el usuario falla en la autenticación

    return render_template('auth/login.html')
