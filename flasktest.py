from flask import Flask, render_template, url_for, flash, redirect
from forms import WeekDayAvail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wlwhfkdm203833yedndnddkj939733heneee'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/avail", methods=["GET", "POST"])
def avail():
    form = WeekDayAvail()
    if form.validate_on_submit():
        flash(f'Thank you, {form.name.data} for submitting your availability!', 'success')
        return redirect(url_for('home'))
    return render_template('avail.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
