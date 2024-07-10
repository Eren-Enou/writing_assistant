from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import Plot, World,Event,Faction, Character
class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    world = QuerySelectField('World', query_factory=lambda: World.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    climate = StringField('Climate', validators=[DataRequired(), Length(max=50)])
    terrain = StringField('Terrain', validators=[DataRequired(), Length(max=50)])
    residents = QuerySelectMultipleField('Residents', query_factory=lambda: Character.query.all(), get_label='name')
    factions = QuerySelectMultipleField('Factions', query_factory=lambda: Faction.query.all(), get_label='name')
    events = QuerySelectMultipleField('Events', query_factory=lambda: Event.query.all(), get_label='name')
    plots = QuerySelectMultipleField('Plots', query_factory=lambda: Plot.query.all(), get_label='name')