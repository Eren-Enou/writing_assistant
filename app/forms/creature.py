from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import Location, Event, Faction

class CreatureForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    world = QuerySelectField('World', query_factory=lambda: World.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    species = StringField('Species', validators=[DataRequired(), Length(max=50)])
    size = StringField('Size', validators=[DataRequired(), Length(max=50)])
    age = IntegerField('Age', validators=[Optional()])
    role = StringField('Role', validators=[DataRequired(), Length(max=50)])
    align = StringField('Alignment', validators=[DataRequired(), Length(max=50)])
    abilities = TextAreaField('Abilities', validators=[Optional()])
    weapons = TextAreaField('Weapons', validators=[Optional()])
    armor = TextAreaField('Armor', validators=[Optional()])
    events = QuerySelectMultipleField('Events', query_factory=lambda: Event.query.all(), get_label='name')
    factions = QuerySelectMultipleField('Factions', query_factory=lambda: Faction.query.all(), get_label='name')
    locations = QuerySelectMultipleField('Locations', query_factory=lambda: Location.query.all(), get_label='name')