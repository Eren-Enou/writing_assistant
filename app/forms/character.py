from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange

class CharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=80)])
    description = TextAreaField('Description', validators=[DataRequired()])
    race = StringField('Race', validators=[DataRequired(), Length(max=80)])
    class_ = StringField('Class', validators=[DataRequired(), Length(max=80)])
    deity = StringField('Deity', validators=[Length(max=80)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=0)])
    alignment = StringField('Alignment', validators=[DataRequired(), Length(max=10)])
    strength = IntegerField('Strength', validators=[DataRequired(), NumberRange(min=0, max=100)])
    dexterity = IntegerField('Dexterity', validators=[DataRequired(), NumberRange(min=0, max=100)])
    constitution = IntegerField('Constitution', validators=[DataRequired(), NumberRange(min=0, max=100)])
    intelligence = IntegerField('Intelligence', validators=[DataRequired(), NumberRange(min=0, max=100)])
    wisdom = IntegerField('Wisdom', validators=[DataRequired(), NumberRange(min=0, max=100)])
    charisma = IntegerField('Charisma', validators=[DataRequired(), NumberRange(min=0, max=100)])
    experience_points = IntegerField('Experience Points', validators=[DataRequired(), NumberRange(min=0)])
    background = TextAreaField('Background', validators=[DataRequired()])
    personality = TextAreaField('Personality', validators=[DataRequired()])
    ideal = TextAreaField('Ideal', validators=[DataRequired()])
    bonds = TextAreaField('Bonds', validators=[DataRequired()])
    flaws = TextAreaField('Flaws', validators=[DataRequired()])
