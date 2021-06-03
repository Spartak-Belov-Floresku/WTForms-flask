from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class PetForm(FlaskForm):
    """generate form to add pet into db"""

    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')])
    photo_url = StringField('URL image', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[NumberRange(0,30, message='The age should be between 0 and 30')])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = SelectField('Available', choices=[('true', 'Available'), ('false', 'Not Available')])