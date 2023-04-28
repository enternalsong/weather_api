from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_restful import Api
from server import app
from data import getrain

CORS(app, resources={r"/.*": {"origins": ["http://127.0.0.1/5173",'http://localhost:5173','http://localhost:5000']}}) 
api = Api(app)
api.add_resource(getrain,'/')

@app.errorhandler(Exception)
def handle_error(error):
    status_code = 500
    if type(error).__name__ == "NotFound":
        status_code = 404
    elif type(error).__name__ == "TypeError":
        status_code = 500
    return jsonify({'msg':type(error).__name__}),status_code

@app.route("/getweather")
def getweather():
    return "getweather"
if __name__ == "__main__":
	app.run(debug=True)