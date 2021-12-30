from flask import (render_template,
                   request,
                   redirect,
                   url_for)
from view.Login import login
from view.registration import register_bp
from Flashcard import Flashcard
from DataBase import app
from FunctionsAdd import *


@app.route("/create-set", methods=['GET', 'POST'])
def create_set():
    return render_template('create-set.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-set', methods=['POST'])
def upload_file():
    name_set = request.form["name_set"]
    description_set = request.form["description"]
    set = SetOfFlas hcards(name_set, 1, description_set)
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


app.register_blueprint(login)
app.register_blueprint(register_bp)

if __name__ == '__main__':
    app.run(debug=True)

