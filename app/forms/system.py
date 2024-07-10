from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class SystemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    rules = TextAreaField('Rules', validators=[Optional()])
    basis = TextAreaField('Basis', validators=[Optional()])
    world_id = IntegerField('World ID', validators=[DataRequired()])