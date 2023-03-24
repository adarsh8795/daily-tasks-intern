from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

    
class StoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
class TagSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str(required= True)

class TagItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)

class UserSchema(Schema):
    id = fields.Int(dump_only = True)
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)
