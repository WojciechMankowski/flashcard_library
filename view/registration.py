from flask import Blueprint, render_template, flash, request
from DataBase import User, db
from Forms import UserForm
from FunctionsAdd import CheckingTheForm

register_bp = Blueprint("register_bp", __name__)

@register_bp.route("/registration", methods=["GET", "POST"])
def registration():
    email = None
    form = UserForm(request.form)
    if request.method == "POST" and CheckingTheForm(form):
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(password=form.password.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()

        email = form.email.data
        form.email.data = ''
        form.password.data = ""
        flash("Zostałeść pomyślnie zerestrowany :)")

    return render_template("registration.html",
                           form=form,
                           email=email,

                           )