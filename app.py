from flask import Flask, render_template, request, redirect, url_for
from SetofFlashcards import SetOfFlashcards
from Flashcard import Flashcard

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
UPLOAD_FOLDER = 'Uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}




@app.route('/')
def index():
    return render_template('upload.html')


def type_check(picture):
    print("type")
    if picture.mimetype[:5] == "image":
        return True
    else:
        print(False)
        return False


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files.getlist('file')
    for picture in uploaded_file:
        if picture.filename != "" and type_check(picture):
            name = picture.filename
            picture.save(f"Uploads/{name}")
    # if uploaded_file.filename != '':
    #     uploaded_file.save(f"Uploads/{uploaded_file.filename}")
    return redirect(url_for('index'))


def itEmpty(list: list[str]) -> bool:
    isEmpty = True
    for index, item in enumerate(list):
        print(item)
        if item == "":
            isEmpty = False
    return isEmpty


@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
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
                print(name)
                picture.save(f"Uploads/{name}")
        if isempty_concept and isempty_definition:
            for index, value in enumerate(concept):
                flashcard = Flashcard(value, definition[index])
                set.Add_flashcard(flashcard)
        else:
            return render_template("index.html", error="Pojawiły się błedy")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
