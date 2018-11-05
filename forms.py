from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, SubmitField, PasswordField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class RegistrationForm(FlaskForm):
    fullName = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    user = RadioField('Choice?', validators=[DataRequired()], choices=[('employee','Employee'), ('employer', 'Employer')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Sign Up')