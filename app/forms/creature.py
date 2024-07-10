from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class CreatureForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    world_id = IntegerField('World ID', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired(), Length(max=50)])
    size = StringField('Size', validators=[DataRequired(), Length(max=50)])
    age = IntegerField('Age', validators=[Optional()])
    role = StringField('Role', validators=[DataRequired(), Length(max=50)])
    align = StringField('Alignment', validators=[DataRequired(), Length(max=50)])
    abilities = TextAreaField('Abilities', validators=[Optional()])
    weapons = TextAreaField('Weapons', validators=[Optional()])
    armor = TextAreaField('Armor', validators=[Optional()])