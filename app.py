from flask import render_template, request, redirect, url_for
from Flashcard import Flashcard
from DataBase import User, app

@app.route("/create-set", methods=['GET', 'POST'])
def create_set():
    return render_template('create-set.html')
@app.route('/')
def index():
    return render_template('upload.html')

@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        if itEmpty(request.form.getlist("email")) and itEmpty(request.form.getlist("password")):
            email = request.form["email"]
            password = request.form["password"]
            user = User(email=email, password=password)
            user.creater_id_user()
        return render_template("registration.html")

@app.route("/login", mimetypes=["GET", "POST"])
def login():
    return render_template("login.html")

def type_check(picture):
    print("type")
    if picture.mimetype[:5] == "image":
        return True
    else:
        return False


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


def itEmpty(list: list[str]) -> bool:
    isEmpty = True
    for index, item in enumerate(list):
        print(item)
        if item == "":
            isEmpty = False
    return isEmpty




if __name__ == '__main__':
    app.run(debug=True)
