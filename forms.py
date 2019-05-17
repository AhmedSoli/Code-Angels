from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Optional

class RequestForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


class AngelForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])