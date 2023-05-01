from flask_restful import Resource,reqparse
from flask import jsonify
from server import db
from models import BaseTable

class getrain(Resource):
    def get(self):
        raindatas = BaseTable.query.all()
        return jsonify({'data':list(map(lambda item: item.serialize(),raindatas))})
