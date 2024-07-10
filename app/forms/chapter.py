from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class ChapterForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    plot_id = IntegerField('Plot ID', validators=[DataRequired()])
    world_id = IntegerField('World ID', validators=[DataRequired()])
    location_id = IntegerField('Location ID', validators=[Optional()])
    creature_id = IntegerField('Creature ID', validators=[Optional()])
    event_id = IntegerField('Event ID', validators=[Optional()])
    magic_system_id = IntegerField('Magic System ID', validators=[Optional()])
    faction_id = IntegerField('Faction ID', validators=[Optional()])