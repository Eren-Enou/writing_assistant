from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import Plot, World, Location, Creature, Faction, Character

class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateTimeField('Date', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    location = QuerySelectField('Location', query_factory=lambda: Location.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    faction = QuerySelectField('Faction', query_factory=lambda: Faction.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    plot = QuerySelectField('Plot', query_factory=lambda: Plot.query.all(), get_label='title', allow_blank=True, validators=[Optional()])
    world = QuerySelectField('World', query_factory=lambda: World.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    characters = QuerySelectMultipleField('Characters', query_factory=lambda: Character.query.all(), get_label='name')
    creatures = QuerySelectMultipleField('Creatures', query_factory=lambda: Creature.query.all(), get_label='name')