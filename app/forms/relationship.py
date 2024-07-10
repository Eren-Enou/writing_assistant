from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class RelationshipForm(FlaskForm):
    character1_id = IntegerField('Character 1 ID', validators=[DataRequired()])
    character2_id = IntegerField('Character 2 ID', validators=[DataRequired()])
    relationship_type = StringField('Relationship Type', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[Optional()])
    level = IntegerField('Level', validators=[Optional(), NumberRange(min=0)])
    is_romantic = BooleanField('Is Romantic', default=False)
    is_supportive = BooleanField('Is Supportive', default=False)
    is_rival = BooleanField('Is Rival', default=False)
    is_ally = BooleanField('Is Ally', default=False)
    is_conflict = BooleanField('Is Conflict', default=False)