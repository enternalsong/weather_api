from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import psycopg2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://heroku-postgres12345678/localhost:rain_hour'
print("success")
db = SQLAlchemy(app)
