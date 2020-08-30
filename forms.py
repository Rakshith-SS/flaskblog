from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField, validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class MakePost(FlaskForm):
    title = StringField('Title', validators= [DataRequired()])
    author = StringField('Author', [validators.Length(min=6, max =20)] )
    message = TextAreaField("Write your Post", validators= [DataRequired()])
    submit = SubmitField('Submit')
