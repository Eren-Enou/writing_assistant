from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class FactionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    world_id = IntegerField('World ID', validators=[DataRequired()])
    is_neutral = BooleanField('Is Neutral', default=False)
    is_good = BooleanField('Is Good', default=False)
    is_evil = BooleanField('Is Evil', default=False)
    is_chaotic = BooleanField('Is Chaotic', default=False)
    is_lawful = BooleanField('Is Lawful', default=False)
    alignment = StringField('Alignment', validators=[Optional(), Length(max=50)])