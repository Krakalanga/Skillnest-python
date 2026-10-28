from flask import Flask
from flask_app.controllers.estudiante_controller import usuario_rutas

app = Flask(__name__, template_folder='views')
app.secret_key = "123"

app.register_blueprint(usuario_rutas)