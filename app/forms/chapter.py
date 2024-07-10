from flask_wtf import FlaskForm
from wtforms import StringField, QuerySelectMultipleField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class ChapterForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    plot = QuerySelectField('Plot', query_factory=lambda: Plot.query.all(), get_label='title', allow_blank=True)
    world = QuerySelectField('World', query_factory=lambda: World.query.all(), get_label='name', allow_blank=True)
    locations = QuerySelectMultipleField('Locations', query_factory=lambda: Location.query.all(), get_label='name')
    creatures = QuerySelectMultipleField('Creatures', query_factory=lambda: Creature.query.all(), get_label='name')
    events = QuerySelectMultipleField('Events', query_factory=lambda: Event.query.all(), get_label='name')
    magic_systems = QuerySelectMultipleField('Magic Systems', query_factory=lambda: System.query.all(), get_label='name')
    factions = QuerySelectMultipleField('Factions', query_factory=lambda: Faction.query.all(), get_label='name')