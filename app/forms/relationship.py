from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, BooleanField, FloatField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField

from app.models import Character

class RelationshipForm(FlaskForm):
    character1 = QuerySelectField('Character 1', query_factory=lambda: Character.query.all(), get_label='name', allow_blank=False)
    character2 = QuerySelectField('Character 2', query_factory=lambda: Character.query.all(), get_label='name', allow_blank=False)
    relationship_type = StringField('Relationship Type', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    level = IntegerField('Level', validators=[Optional()])
    is_romantic = BooleanField('Is Romantic')
    is_supportive = BooleanField('Is Supportive')
    is_rival = BooleanField('Is Rival')
    is_ally = BooleanField('Is Ally')
    is_conflict = BooleanField('Is Conflict')