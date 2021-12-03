from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CreateDivisionForm(FlaskForm):
    weight_range = SelectField('Weight Class', validators=[DataRequired()],
        choices=[
            ('Lightweight', 'Lightweight (131-140lbs)'),
            ('Welterweight', 'Welterweight (141-147lbs)'),
            ('Middleweight', 'Middleweight (148-168lbs)'),
            ('Light Heavyweight', 'Light Heavyweight (169-175lbs)'),
            ('Cruiserweight', 'Cruiserweight (176-200lbs)'),
            ('Heavyweight', 'Heavyweight (>201lbs)')
        ]
    )
    name = StringField('Division Name', validators=[DataRequired()])
    submit = SubmitField('Add Division')

class CreateBoxerForm(FlaskForm):
    name = StringField('Boxer Name', validators=[DataRequired()])
    weight = IntegerField('Boxer Weight', validators=[DataRequired()])
    division = SelectField('Boxer Weight Class', validators=[DataRequired()], 
        choices=[
            ('Lightweight', 'Lightweight (131-140lbs)'),
            ('Welterweight', 'Welterweight (141-147lbs)'),
            ('Middleweight', 'Middleweight (148-168lbs)'),
            ('Light Heavyweight', 'Light Heavyweight (169-175lbs)'),
            ('Cruiserweight', 'Cruiserweight (176-200lbs)'),
            ('Heavyweight', 'Heavyweight (>201lbs)')
        ]
    )
    submit = SubmitField('Add Boxer')