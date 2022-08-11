from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, EqualTo
from wtforms.widgets import TextArea
class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()] )
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description',widget=TextArea(), validators=[DataRequired()])
    img_file = FileField("Image",validators=[DataRequired()])
    submit = SubmitField('Submit')  

class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')