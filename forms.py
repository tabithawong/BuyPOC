from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, ValidationError


class SubmitBusinessForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    website = StringField("Website", validators=[DataRequired()])
    category = SelectField("Category", choices=[("Restaurants", "Restaurants"), ("Cafes", "Cafes"), ("Specialty Goods", "Specialty Goods"), ("Apparel", "Apparel"), ("Lifestyle", "Lifestyle")])
    address = StringField("Address", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    submit = SubmitField("Submit")


class FilterForm(FlaskForm):
    restaurants = BooleanField("Restaurants")
    cafes = BooleanField("Cafes")
    specialty_goods = BooleanField("Specialty Goods")
    apparel = BooleanField("Apparel")
    lifestyle = BooleanField("Lifestyle")
    submit = SubmitField("Submit")