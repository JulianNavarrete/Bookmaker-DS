from marshmallow import Schema, fields


class ClienteSchema(Schema):

    id = fields.Integer(dump_only=True)
    apellido = fields.String(required=True)
    nombre = fields.String(required=True)
    mail = fields.String(required=True)
