from marshmallow import Schema, fields


class ResultSchema(Schema):
    title = fields.String(required=True)
    summary = fields.String(required=True)

    class Meta:
        unknown = 'exclude'
