from flask import Blueprint, render_template, request, redirect
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante


usuario_rutas = Blueprint('usuario_rutas', __name__)


@usuario_rutas.route('/cursos')
def index():
    cursos = Curso.get_all()
    return render_template('index.html', todos_cursos=cursos)

@usuario_rutas.route('/crear/curso', methods=['POST'])
def crear_curso():
    Curso.save(request.form)
    return redirect('/cursos')

@usuario_rutas.route('/cursos/<int:id>')
def mostrar_curso(id):
    data = {
        'id': id
    }
    curso = Curso.get_one_with_students(data)
    return render_template('mostrar_curso.html', curso=curso)

@usuario_rutas.route('/nuevo/estudiante')
def nuevo_estudiante():
    cursos = Curso.get_all()
    return render_template('nuevo_estudiante.html', todos_cursos=cursos)

@usuario_rutas.route('/crear/estudiante', methods=['POST'])
def crear_estudiante():
    Estudiante.save(request.form)
    return redirect(f"/cursos/{request.form['curso_id']}")