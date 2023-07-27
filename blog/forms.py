from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])

    name = StringField("Name",
                       validators=[
                           DataRequired(),
                           EqualTo(
                               'confirm_username',
                               message='Usernames do not match. Try again'
                           )
                       ])
    confirm_username = StringField("Confirm your name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Regexp(
                               '^[a-z]{6,8}$',
                               message='Your password should be between 6 to 8 characters long, and can only contain '
                                       'lowercase letters. '
                           )])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

