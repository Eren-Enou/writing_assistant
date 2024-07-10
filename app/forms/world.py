from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class WorldForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    history = TextAreaField('History', validators=[Optional()])
    time_period = StringField('Time Period', validators=[Optional(), Length(max=50)])
    setting = StringField('Setting', validators=[Optional(), Length(max=50)])
    temperature = FloatField('Temperature', validators=[Optional()])
    humidity = FloatField('Humidity', validators=[Optional()])
    flora = TextAreaField('Flora', validators=[Optional()])
    fauna = TextAreaField('Fauna', validators=[Optional()])
    magical_system = StringField('Magical System', validators=[Optional(), Length(max=100)])