from flask import Blueprint,request, render_template


blueprints_login = Blueprint('login', __name__, url_prefix="/")

blueprints_login.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

