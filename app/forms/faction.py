from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import World, Event, Character

class FactionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    world = QuerySelectField('World', query_factory=lambda: World.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    is_neutral = BooleanField('Is Neutral')
    is_good = BooleanField('Is Good')
    is_evil = BooleanField('Is Evil')
    is_chaotic = BooleanField('Is Chaotic')
    is_lawful = BooleanField('Is Lawful')
    alignment = StringField('Alignment', validators=[Optional(), Length(max=50)])
    characters = QuerySelectMultipleField('Characters', query_factory=lambda: Character.query.all(), get_label='name')
    events = QuerySelectMultipleField('Events', query_factory=lambda: Event.query.all(), get_label='name')