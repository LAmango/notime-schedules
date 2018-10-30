from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'wlwhfkdm203833yedndnddkj939733heneee'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/avail")
def avail():
    return render_template('avail.html')

if __name__ == '__main__':
    app.run(debug=True)
