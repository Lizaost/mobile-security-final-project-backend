from marshmallow import Schema, fields


class LectureSchema(Schema):
    id = fields.Int()
    slug = fields.Str()
    title = fields.Str()
    cover = fields.Str()
    is_visible = fields.Bool()
    order = fields.Int()
