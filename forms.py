from flask_wtf import FlaskForm
from wtfforms import BooleanField

class WeekDayAvail(FlaskForm):
    sunday = BooleanField('Sunday')
    