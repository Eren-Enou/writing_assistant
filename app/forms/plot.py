
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import World, Location, Event, Character

class PlotForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    world = QuerySelectField('World', query_factory=lambda: World.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    status = StringField('Status', validators=[Optional(), Length(max=50)])
    genre = StringField('Genre', validators=[Optional(), Length(max=50)])
    rating = IntegerField('Rating', validators=[Optional()])
    word_count = IntegerField('Word Count', validators=[Optional()])
    reading_time = IntegerField('Reading Time', validators=[Optional()])
    published_date = DateTimeField('Published Date', format='%Y-%m-%d', validators=[Optional()])

    # Multiple Select Fields
    locations = QuerySelectMultipleField('Locations', query_factory=lambda: Location.query.all(), get_label='name')
    events = QuerySelectMultipleField('Events', query_factory=lambda: Event.query.all(), get_label='name')
    characters = QuerySelectMultipleField('Characters', query_factory=lambda: Character.query.all(), get_label='name')