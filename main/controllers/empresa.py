from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import EmpresaModel
from main.map import EmpresaSchema
from main.services import EmpresaService

empresa_schema = EmpresaSchema()
empresa_service = EmpresaService()


class Empresa(Resource):

    def get(self, id):
        return empresa_schema.dump(empresa_service.obtener_empresa_por_id(id))

    def delete(self, id):
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        try:
            db.session.delete(empresa)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        empresa = db.session.query(EmpresaModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(empresa, key, value)
        try:
            db.session.add(empresa)
            db.session.commit()
            return empresa_schema .dump(empresa), 201
        except:
            return '', 404


class Empresas(Resource):

    def get(self):
        return empresa_schema.dump(empresa_service.obtener_empresas(), many=True)

    def post(self):
        empresas = empresa_schema.load(request.get_json())
        try:
            db.session.add(empresas)
            db.session.commit()
            return empresa_schema.dump(empresas), 201
        except:
            return '', 404

