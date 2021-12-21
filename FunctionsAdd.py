import re
import Forms


def type_check(picture):
    print("type")
    if picture.mimetype[:5] == "image":
        return True
    else:
        return False

def itEmpty(list: list[str]) -> bool:
    isEmpty = True
    for index, item in enumerate(list):
        if item == "":
            isEmpty = False
    return isEmpty

def __checkEmail(email: str) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def CheckingTheForm(form: Forms.UserForm) -> bool:
    print(type(form))
    if form.password.data != "" and  (len(form.password.data) > 5 or len(form.password.data)<10):
        if __checkEmail(form.email.data):
            return True
        else:
            return False
    else:
        return False
