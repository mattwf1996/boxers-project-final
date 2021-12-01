from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BoxerForm(FlaskForm):
    description = StringField("Boxer Description", validators=[DataRequired()])
    submit = SubmitField("Add Boxer")