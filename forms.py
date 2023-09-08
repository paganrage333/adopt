from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, URL, AnyOf, Optional, NumberRange

class AddPetForm(FlaskForm):

    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Pet species", validators=[AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = FloatField("Pet age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Any notes")

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available")