
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class PlotForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    world_id = IntegerField('World ID', validators=[DataRequired()])
    status = StringField('Status', validators=[Optional(), Length(max=50)])
    genre = StringField('Genre', validators=[Optional(), Length(max=50)])
    rating = IntegerField('Rating', validators=[Optional(), NumberRange(min=0, max=10)])
    word_count = IntegerField('Word Count', validators=[Optional()])
    reading_time = IntegerField('Reading Time', validators=[Optional()])
    published_date = DateTimeField('Published Date', format='%Y-%m-%d', validators=[Optional()])