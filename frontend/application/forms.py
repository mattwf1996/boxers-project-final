from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CreateDivisionForm(FlaskForm):
    name = StringField('Division Name', validators=[DataRequired()])
    mass = IntegerField('Division Weight_Range', validators=[DataRequired()],
        choices=[
            ('Lightweight', 'Lightweight'),
            ('Middleweight', 'Middleweight'),
            ('Heavyweight', 'Heavyweight')
        ]
    )
    submit = SubmitField('Add Division')

class CreateBoxerForm(FlaskForm):
    name = StringField('Boxer Name', validators=[DataRequired()])
    weight = IntegerField('Boxer Weight', validators=[DataRequired()])
    division = SelectField('Boxer Division', validators=[DataRequired()], choices=[])
    submit = SubmitField('Add Boxer')








# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# class BoxerForm(FlaskForm):
#     description = StringField("Boxer Description", validators=[DataRequired()])
#     submit = SubmitField("Add Boxer")