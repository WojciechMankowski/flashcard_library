from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20),unique=True, nullable=False )
    email = db.Column(db.String(120), unique=True, nullable=False)

class SetOfFlashcardsModels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    name_set = db.Column(db.String(100), unique=True, nullable=False)
    description  = db.Column(db.TEXT, unique=True, nullable=False)
    image =
