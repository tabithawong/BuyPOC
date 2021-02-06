from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, ValidationError


class SubmitBusinessForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    website = StringField("Website", validators=[DataRequired()])
    category = SelectField("Category", choices=[("Restaurants", "Restaurants"), ("Cafes", "Cafes"), ("Specialty Goods", "Specialty Goods"), ("Apparel", "Apparel"), ("Lifestyle", "Lifestyle")])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Submit")