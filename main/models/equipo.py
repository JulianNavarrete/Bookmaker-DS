from main import db


class Equipo(db.Model):

    __id = db.Column(db.Integer, primary_key=True)
    __nombre = db.Column(db.String(50), nullable=False)
    __escudo = db.Column(db.String(50), nullable=False)
    __pais = db.Column(db.String(120), nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__mail} >'

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_escudo(self, escudo):
        self.__escudo = escudo

    def get_escudo(self):
        return self.__escudo

    def set_pais(self, pais):
        self.__pais = pais

    def get_pais(self):
        return self.__pais

