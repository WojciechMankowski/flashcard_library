from sqlalchemy import Column, String, Integer
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
Bootstrap(app)
name_file = 'test.db'
path = "C:\\Users\\wojte\\PycharmProjects\\siszkarty\\test.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{path}"
db = SQLAlchemy(app)

class User(db.Model):
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(20),unique=True, nullable=False )
    email = Column(String(120), unique=True, nullable=False)

    def __init__(self,  password: str,email: str):
        self.id = self.creater_id()
        self.id_user = self.creater_id_user()
        self.username = email
        self.password = password
        self.email = email

    def __repr__(self):
        return f'User {self.username}'

    def creater_id_user(self):
        query = User.query.all()
        data = query[len(query)-1]
        return data.id_user +1
    def creater_id(self):
        query = User.query.all()
        data = query[len(query)-1]
        return data.id +1

# class SetOfFlashcardsModels(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
#     name_set = db.Column(db.String(100), unique=True, nullable=False)
#     description  = db.Column(db.TEXT, unique=True, nullable=False)
#     image = db.Column(db.String(250) ,unique=True, nullable=False)
#
# db.create_all()


