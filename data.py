from flask_restful import Resource,reqparse
from flask import jsonify
from server import db
from models import BaseTable
# from models import animalModel

class getrain(Resource):
    def get(self):
        raindatas = BaseTable.query.all()
        # newrain={}
        # for item in raindatas:
        #     serialized_data = item.serialize()
        #
        return jsonify({'data':list(map(lambda item: item.serialize(),raindatas))})
