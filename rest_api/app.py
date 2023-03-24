import os

from flask import Flask
from flask_smorest import Api  #connects the flask-smorest exttension to flask app
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from blocklist import BLOCKLIST
import secrets
from flask_migrate import Migrate

from db import db

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
# from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint

def create_app(db_url = None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    migrate = Migrate(app,db)
    api = Api(app)  ##connects the flask-smorest exttension to flask app

    # app.config["JWT_SECRET_KEY"] = "jose"
    app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128)

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    # api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)


    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )
    
    return app











# @app.get("/stores/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         return {'message':'store not found'},404


# @app.get("/store")  # "/store is an endpoint which calls the get_store method"
# def get_stores():   # function associated with the end point 
#     return { "stores" : list(stores.values()) }


# #json is string of text in  not a python dict

# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     store_id=uuid.uuid4().hex
#     # new_store = { "name ": my_data["name"] ,"item": [] }
#     new_store = {**store_data,"id" : store_id}
#     stores[store_id]=new_store
#     # stores.append(new_store)
#     return new_store,201

# @app.post("/item")
# def create_items(name):  
#     item_data=request.get_json()
#     if item_data["store_id"] not in stores:
#             return {"message":"store not found"},404
#     item_id=uuid.uuid4().hex
#     item={**item_data,"id" :item_id}
#     items[item_id]=item
#     return item,201
#     #     # if store["name"] == name:
#     #     #     new_item = {"name":request_data["name"],"price":request_data["price"]}
#     #     #     store["item"].append(new_item)
#     #         return new_item,201
#     # return {"message":"store not found"},404    
            





