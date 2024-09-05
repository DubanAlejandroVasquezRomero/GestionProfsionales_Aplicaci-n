from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.auth import login_required
from app.db import get_db

bp = Blueprint ('admin',__name__,url_prefix= '/Admin')

@bp.route ('/dashboard')
@login_required
def dashboard ():
    return render_template ("admin/dashboard.html")

@bp.route ('/editar_usuario/<int:usuario_id>/editar',methods = ['POST','GET'])
@login_required
def editar_usuario  (usuario_id):
    db, c = get_db ()
    c.execute('SELECT * FROM usuarios WHERE id = %s', (usuario_id,))
    usuario = c.fetchone()

    if request.method == 'POST':
        nombre = request.form ['Nombre']
        correo = request.form ['Correo']
        rol = request.form ['Rol']

        c.execute(
            'UPDATE usuarios SET nombre = %s, correo = %s, rol = %s WHERE id = %s',
            (nombre, correo, rol, usuario_id)
        )
        db.commit()
        flash ("Usuario editado con exito")
        return redirect (url_for('admin.usuarios'))
    return render_template ('admin/editar_usuario.html',usuario=usuario)




@bp.route ('/usuarios')
@login_required
def usuarios ():
    db , c = get_db ()
    c.execute ('SELECT * FROM usuarios')
    users = c.fetchall ()
    return render_template ('admin/usuarios.html',usuarios=users)

@bp.route ('/usuarios/eliminar/<int:id>',methods = ['POST'])
@login_required
def eliminar_usuario (id):
    db,c = get_db ()
    c.execute ('DELETE FROM usuarios WHERE id = %s',(id,))
    db.commit()
    flash ('Usuario eliminado Con Exito')
    return redirect (url_for('admin.usuarios'))



