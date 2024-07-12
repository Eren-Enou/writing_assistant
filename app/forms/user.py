from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, IntegerField, SubmitField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional, ValidationError, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from ..models import User

class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=128)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=128)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    submit = SubmitField('Login')