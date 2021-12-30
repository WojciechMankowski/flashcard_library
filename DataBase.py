from sqlalchemy import Column, String, Integer
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
path = r"E:\projekty\fiszkiFlask\db.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{path}"
app.config["SECRET_KEY"] = '571ebf8e13ca209536c29be68d435c00'
db = SQLAlchemy(app)



class User(db.Model):
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    password = Column(String(20),unique=True, nullable=False )
    email = Column(String(120), unique=True, nullable=False)

    def __init__(self,  password: str,email: str):
        self.id = self.creater_id()
        self.id_user = self.creater_id()
        self.password = password
        self.email = email

    def __repr__(self):
        return f"User: {self.email}"

    def creater_id(self):
        query = User.query.all()
        if len(query) == 0:
            return 1
        else:
            data = query[len(query)-1]
            return data.id +1

def login_validator(email: str, password:str):
    query = User.query.filter_by(email=email).first()
    if query != None:
        if query.password == password:
            return True
        else:
            return False
    else:
        return False

# class SetOfFlashcardsModels(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
#     name_set = db.Column(db.String(100), unique=True, nullable=False)
#     description  = db.Column(db.TEXT, unique=True, nullable=False)
#     image = db.Column(db.String(250) ,unique=True, nullable=False)
#
# db.create_all()


