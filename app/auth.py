import functools 
from functools import wraps

from flask import (
    Blueprint,render_template, request, redirect,url_for, flash, session, g
)

from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

bp = Blueprint ('auth',__name__)

@bp.route ('/register', methods = ['GET','POST'])
def register ():
    if request.method == 'POST':
        nombre = request.form ['nombre']
        correo = request.form ['correo']
        contraseña = request.form ['contraseña']
        db,c = get_db ()
        error = None

        if not nombre or not correo or not contraseña:
            error = 'Por favor complete todos los campos'
        else:
            c.execute(
                'SELECT id FROM usuarios WHERE correo = %s',(correo,)
            )
            if c.fetchone () is not None:
                error = 'El correo ya esta registrado'
        if error is None:
            c.execute(
                'INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)',
                (nombre, correo, generate_password_hash(contraseña))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        
        flash(error)
    return render_template ("auth/register.html")


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Nombre = request.form.get('nombre')
        contraseña = request.form.get('contraseña')
        db, c = get_db()
        error = None
        c.execute(
            'SELECT * FROM usuarios WHERE nombre = %s', (Nombre,)
        )
        user = c.fetchone()

        if user is None:
            error = 'Usuario y/o contraseña inválida'
        elif not check_password_hash(user['contraseña'], contraseña):
            error = 'Usuario y/o contraseña inválida'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('admin.dashboard'))
        
        flash(error)

    return render_template('auth/login.html')


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes estar logueado para acceder a esta página.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


