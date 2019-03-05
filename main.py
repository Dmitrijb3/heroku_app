from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")  #controller / Kas sakas ar @ - decorators
def about():
    return render_template('about.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)