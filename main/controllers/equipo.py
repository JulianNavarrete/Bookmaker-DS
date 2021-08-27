from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import EquipoModel
from main.map import EquipoSchema

equipo_schema = EquipoSchema()


class Equipos(Resource):

    def get(self):
        equipo = db.session.query(EquipoModel)
        return equipo_schema.dump(equipo, many=True)

    def post(self):
        equipo = equipo_schema.load(request.get_json())
        try:
            db.session.add(equipo)
            db.session.commit()
            return equipo_schema.dump(equipo), 201
        except:
            return '', 404


class Equipo(Resource):

    def get(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        return equipo_schema.dump(equipo)

    def delete(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        try:
            db.session.delete(equipo)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(equipo, key, value)
        try:
            db.session.add(equipo)
            db.session.commit()
            return equipo_schema.dump(equipo), 201
        except:
            return '', 404

