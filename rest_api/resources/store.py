from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from models.store import StoreModel

blp = Blueprint("stores",__name__,description ="operation on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self,store_id):
        try:
           return stores[store_id]
        except KeyError:
           return {'message':'store not found'},404

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message":"store deleted"}
        except KeyError:
            return {'message':'store not found'},404
