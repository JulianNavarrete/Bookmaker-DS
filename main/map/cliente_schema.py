from marshmallow import Schema, fields, validate, post_load
from main.models import ClienteModel


class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    apellido = fields.Str(required=True)
    nombre = fields.Str(required=True)
    mail = fields.Str(required=True, validate=validate.Email())

    @post_load
    def make_cliente(self, data, **kwargs):
        return ClienteModel(**data)

