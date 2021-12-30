from flask import (Blueprint,
                   request,
                   render_template,
                   flash,
                   redirect,
                   url_for,
                   session)
from DataBase import User, login_validator
from Forms import UserForm



login = Blueprint("login", __name__)

@login.route("/login", methods=["GET", "POST"])
def login_def():
    form = UserForm(request.form)
    if request.method == "POST" and login_validator(form.email.data, form.password.data):
        flash("Zostałeść zalogowany")
        session["user"] = form.email.data
        return redirect(url_for("index"))
    return render_template("login.html", form=form)




