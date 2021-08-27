import os
from flask import Flask
from dotenv import load_dotenv
# Importar librería flask_restful
from flask_restful import Api
# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Inicializar API de Flask Restful
api = Api()
# Inicializar SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Url de configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME')
    db.init_app(app)

    # Importar directorio de recursos
    import main.controllers as resources

    # Cargar a la API el Recurso Clientes e indicar ruta
    api.add_resource(resources.ClientesResource, '/clientes')
    # Cargar a la API el Recurso Cliente e indicar ruta
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    api.add_resource(resources.EquiposResource, '/equipos')
    api.add_resource(resources.EmpresasResource, '/empresas')
    api.add_resource(resources.EmpresaResource, '/empresa/<id>')

    # Cargar la aplicación en la API de Flask Restful
    api.init_app(app)
    return app
