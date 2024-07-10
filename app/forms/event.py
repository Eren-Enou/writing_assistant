from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateTimeField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    location_id = IntegerField('Location ID', validators=[Optional()])
    faction_id = IntegerField('Faction ID', validators=[Optional()])
    plot_id = IntegerField('Plot ID', validators=[Optional()])
    world_id = IntegerField('World ID', validators=[DataRequired()])