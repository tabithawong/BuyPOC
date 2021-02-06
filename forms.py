from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, ValidationError


class SubmitBusinessForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")