from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    world_id = IntegerField('World ID', validators=[DataRequired()])
    climate = StringField('Climate', validators=[DataRequired(), Length(max=50)])
    terrain = StringField('Terrain', validators=[DataRequired(), Length(max=50)])