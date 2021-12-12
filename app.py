from flask import Flask, render_template, request
from SetofFlashcards import SetOfFlashcards
from Flashcard import Flashcard

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


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

        if isempty_concept and isempty_definition:
            for index, value in enumerate(concept):
                flashcard = Flashcard(value, definition[index])
                set.Add_flashcard(flashcard)
        else:
            return render_template("index.html", error="Pojawiły się błedy")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
