from flask import Blueprint, render_template, request, redirect, url_for
from flask_app.models.usuario import Usuario

usuario_rutas = Blueprint('usuario', __name__, url_prefix='/usuarios')


@usuario_rutas.route('/')
def index():
    usuarios = Usuario.get_all()
    return render_template('index.html', todos_los_usuarios=usuarios)


@usuario_rutas.route('/nuevo')
def nuevo():
    return render_template('nuevo.html')


@usuario_rutas.route('/crear', methods=['POST'])
def crear():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    nuevo_id = Usuario.save(data)
    return redirect(url_for('usuario.mostrar_usuario', id=nuevo_id))


@usuario_rutas.route('/<int:id>')
def mostrar_usuario(id):
    usuario = Usuario.get_by_id(id)
    if not usuario:
        return redirect(url_for('usuario.index'))
    return render_template('mostrar.html', usuario=usuario)


@usuario_rutas.route('/<int:id>/editar')
def editar(id):
    usuario = Usuario.get_by_id(id)
    if not usuario:
        return redirect(url_for('usuario.index'))
    return render_template('editar.html', usuario=usuario)


@usuario_rutas.route('/<int:id>/actualizar', methods=['POST'])
def actualizar(id):
    data = {
        "id": id,
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.update(data)
    return redirect(url_for('usuario.mostrar_usuario', id=id))


@usuario_rutas.route('/<int:id>/eliminar', methods=['POST'])
def eliminar(id):
    Usuario.delete(id)
    return redirect(url_for('usuario.index'))