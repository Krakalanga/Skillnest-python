from flask_app.config.mysqlconnection import connectToMySQL

db = 'esquema_usuarios'

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    #obtener todos los usuarios
    def get_all(cls):
        query = "SELECT * FROM usuarios"
        mysql = connectToMySQL(db)
        resultados = mysql.query_db(query)
        return [cls(fila) for fila in resultados]

    @classmethod 
    #obtener datos usuario por id
    def get_by_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id=%(id)s "
        data = {"id": id}
        mysql = connectToMySQL(db)
        resultado = mysql.query_db(query, data)
        if resultado:
            return cls(resultado[0])
        return None
    
    @classmethod
    #insertar datos a la tabla usuarios
    def save(cls, data):
        query = ("INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at) " 
                 "VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW()) ")
        mysql = connectToMySQL(db)
        return mysql.query_db(query, data)

    @classmethod
    #eliminar usuario
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id=%(id)s"
        data = {"id": id}
        mysql = connectToMySQL(db)
        return mysql.query_db(query, data)
    