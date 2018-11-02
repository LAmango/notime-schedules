from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class WeekDayAvail(FlaskForm):
    name = StringField('Enter name here...', validators=[DataRequired()])

    sunday = BooleanField('Sunday')

    monday = BooleanField('Monday')

    tuesday = BooleanField('Tuesday')

    wednesday = BooleanField('Wednesday')

    thursday = BooleanField('Thrusday')

    friday = BooleanField('Friday')

    saturday = BooleanField('Saturday')

    submit = SubmitField('Submit')
    