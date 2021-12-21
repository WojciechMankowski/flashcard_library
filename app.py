from flask import render_template, request, redirect, url_for, flash
from Flashcard import Flashcard
from DataBase import User, app, db
from Forms import UserForm
from FunctionsAdd import *

@app.route("/create-set", methods=['GET', 'POST'])
def create_set():
    return render_template('create-set.html')

@app.route('/')
def index():
    return render_template('upload.html')

@app.route("/registration", methods=["GET", "POST"])
def reg():
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

# def registration():
#     if request.method == "POST":
#         if itEmpty(request.form.getlist("email")) and itEmpty(request.form.getlist("password")):
#             email = request.form["email"]
#             password = request.form["password"]
#             user = User(email=email, password=password)
#         return render_template("registration.html")

# @app.route("/login", mimetypes=["GET", "POST"])
# def login():
#     return render_template("login.html")

@app.route('/create-set', methods=['POST'])
def upload_file():
    name_set = request.form["name_set"]
    description_set = request.form["description"]
    set = SetOfFlashcards(name_set, 1, description_set)
    concept = request.form.getlist('concept')
    definition = request.form.getlist('definition')
    isempty_concept = itEmpty(concept)
    isempty_definition = itEmpty(definition)
    uploaded_file = request.files.getlist('file')
    for picture in uploaded_file:
        if picture.filename != "" and type_check(picture):
            name = picture.filename
            picture.save(f"Uploads/{name}")
        else:
            return render_template("index.html", error="Pojawiły się błedy")
    if isempty_concept and isempty_definition:
        for index, value in enumerate(concept):
            flashcard = Flashcard(value, definition[index])
            set.Add_flashcard(flashcard)
    else:
        return render_template("index.html", error="Pojawiły się błedy")
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
