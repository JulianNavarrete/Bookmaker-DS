from main import db


class Cliente(db.Model):

    __id = db.Column('id', db.Integer, primary_key=True)
    __apellido = db.Column('apellido', db.String(50), nullable=False)
    __nombre = db.Column('nombre', db.String(50), nullable=False)
    __mail = db.Column('mail', db.String(120), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__mail} >'

    def to_json(self):
        cliente_json ={
            'id': self.__id,
            'apellido': self.__apellido,
            'nombre': self.__nombre,
            'mail': self.__mail
        }

    @staticmethod
    def from_json(cliente_json):
        id = cliente_json.get('id')
        apellido = cliente_json.get('apellido')
        nombre = cliente_json.get('nombre')
        mail = cliente_json.get('mail')
        return Cliente(id=id,
                       apellido=apellido,
                       nombre=nombre,
                       mail=mail,
                       )
    
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apellido(self):
        return self.__apellido

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_mail(self, mail):
        self.__mail = mail

    def get_mail(self):
        return self.__mail
