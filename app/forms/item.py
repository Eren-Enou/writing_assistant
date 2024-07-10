from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    item_type = StringField('Type', validators=[DataRequired(), Length(max=50)])
    weight = FloatField('Weight', validators=[Optional()])
    value = IntegerField('Value', validators=[Optional()])
    enchantment = StringField('Enchantment', validators=[Optional(), Length(max=50)])
    owner_id = IntegerField('Owner ID', validators=[Optional()])