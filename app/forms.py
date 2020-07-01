from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User
from wtforms.validators import Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('ReEnter Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    #the next two functions are directly invoked by WTForms because of using validate<fieldName> as funcn
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user != None:
            raise ValidationError('Please use a different Username')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user != None:
            raise ValidationError('Please use a different email address')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    about_me = TextAreaField('About Me', validators = [Length(min = 0, max = 140)])
    submit = SubmitField('Submit')
    
