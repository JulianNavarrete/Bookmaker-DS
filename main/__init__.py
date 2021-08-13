import os
from flask import Flask
from dotenv import load_dotenv
# Importar librería flask_restful
from flask_restful import Api
# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Importar Flask JWT
# Importo PyMySQL
# import PyMySQL

# Inicializar API de Flask Restful
api = Api()
# Inicializar SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Para SQL Alchemy
    # Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Url de configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME')
    db.init_app(app)

    # Para MySQL



    # Importar directorio de recursos
    import main.controllers as resources

    # Cargar a la API el Recurso Bolsones e indicar ruta
    api.add_resource(resources.BolsonesResource, '/bolsones')
    # Cargar a la API el Recurso Bolsón e indicar ruta
    api.add_resource(resources.BolsonResource, '/bolson/<id>')
    api.add_resource(resources.BolsonesPendientesResource, '/bolsones-pendientes')
    api.add_resource(resources.BolsonPendienteResource, '/bolson-pendiente/<id>')
    api.add_resource(resources.BolsonesPreviosResource, '/bolsones-previos')
    api.add_resource(resources.BolsonPrevioResource, '/bolson-previo/<id>')
    api.add_resource(resources.BolsonesVentaResource, '/bolsones-venta')
    api.add_resource(resources.BolsonVentaResource, '/bolson-venta/<id>')
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.add_resource(resources.ComprasResource, '/compras')
    api.add_resource(resources.CompraResource, '/compra/<id>')
    api.add_resource(resources.ProductosResource, '/productos')
    api.add_resource(resources.ProductoResource, '/producto/<id>')

''' 
    from main.auth import routes
    # Importar blueprint
    app.register_blueprint(auth.routes.auth)
'''

    # Cargar la aplicación en la API de Flask Restful
    api.init_app(app)
    return app
