from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import World

class SystemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rules = TextAreaField('Rules')
    basis = TextAreaField('Basis')
    worlds = QuerySelectMultipleField('Worlds', query_factory=lambda: World.query.all(), get_label='name')