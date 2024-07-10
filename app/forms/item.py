from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import Character, Location, Event

class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    item_type = StringField('Type', validators=[DataRequired(), Length(max=50)])
    weight = FloatField('Weight', validators=[Optional()])
    value = IntegerField('Value', validators=[Optional()])
    enchantment = StringField('Enchantment', validators=[Optional(), Length(max=50)])
    owner = QuerySelectField('Owner', query_factory=lambda: Character.query.all(), get_label='name', allow_blank=True, validators=[Optional()])
    locations = QuerySelectMultipleField('Locations', query_factory=lambda: Location.query.all(), get_label='name')
    events = QuerySelectMultipleField('Events', query_factory=lambda: Event.query.all(), get_label='name')
