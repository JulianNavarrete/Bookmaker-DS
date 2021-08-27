from main import db


class Equipo(db.Model):

    __tablename__ = 'equipos'
    __id = db.Column(db.Integer, primary_key=True)
    __nombre = db.Column(db.String(50), nullable=False)
    __escudo = db.Column(db.String(50), nullable=False)
    __pais = db.Column(db.String(120), nullable=False)
    __puntaje = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, escudo, pais):
        self.__nombre = nombre
        self.__escudo = escudo
        self.__pais = pais

    def __repr__(self):
        return f'<Equipo: {self.__nombre} {self.__escudo} {self.__pais} >'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo

    @escudo.deleter
    def escudo(self):
        del self.__escudo

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @pais.deleter
    def pais(self):
        del self.__pais

