from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class UserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),
                                             Email(message="Niepoprawny adres email")])
    password = PasswordField("pasword", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    sumbit = SubmitField("sumbit")