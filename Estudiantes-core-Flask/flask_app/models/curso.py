from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import estudiante

class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.estudiantes = [] 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        cursos = []
        for curso in results:
            cursos.append(cls(curso))
        return cursos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)

    @classmethod
    def get_one_with_students(cls, data):
        query = "SELECT * FROM cursos LEFT JOIN estudiantes ON cursos.id = estudiantes.curso_id WHERE cursos.id = %(id)s;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        
        if results:
            curso = cls(results[0])
            for row in results:
                if row['estudiantes.id'] is not None:
                    student_data = {
                        'id': row['estudiantes.id'],
                        'nombre': row['estudiantes.nombre'],
                        'apellido': row['apellido'],
                        'edad': row['edad'],
                        'created_at': row['estudiantes.created_at'],
                        'updated_at': row['estudiantes.updated_at'],
                        'curso_id': row['curso_id']
                    }
                    curso.estudiantes.append(estudiante.Estudiante(student_data))
            return curso
        return None