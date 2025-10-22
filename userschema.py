from app import ma
from marshmallow import fields, validate

class UserSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required = True, validate = validate.Length(min=3, max=100))
    email = fields.Email(required = True, validate = validate.Length(max=120))
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=8))

    class Meta:
        fields = ("id", "username", "email")
        ordered = True