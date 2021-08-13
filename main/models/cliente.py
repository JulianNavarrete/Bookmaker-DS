from main import db


class Cliente(db.Model):

    __id = db.Column(db.Integer, primary_key=True)
    __apellido = db.Column(db.String(50), nullable=False)
    __nombre = db.Column(db.String(50), nullable=False)
    __mail = db.Column(db.String(120), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__mail} >'

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
