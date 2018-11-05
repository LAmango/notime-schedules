from flask import Flask, render_template, url_for, flash, redirect
from forms import WeekDayAvail, RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wlwhfkdm203833yedndnddkj939733heneee'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', Title='Home')

@app.route("/login", methods=["GET", "POST"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        if login.email.data == "lucas@albano.us" and login.password.data == "password":
            return redirect(url_for('home'))
    return render_template('login.html', Title='Login', form=login)

@app.route("/register", methods=["GET", "POST"])
def register():
    register = RegistrationForm()
    if register.validate_on_submit():
        flash(f'name: {register.fullName.data}, usertype: {register.user.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', Title='Register', form=register)

@app.route("/avail", methods=["GET", "POST"])
def avail():
    form = WeekDayAvail()
    if form.validate_on_submit():
        flash(f'Thank you, {form.name.data} for submitting your availability!', 'success')
        return redirect(url_for('home'))
    return render_template('avail.html', Title='Availablility', form=form)

if __name__ == '__main__':
    app.run(debug=True)
