from flask import Flask, session, render_template, request, redirect, url_for
from models import User
import hashlib
import uuid
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")  #controller / Kas sakas ar @ - decorators
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/portfolio_details")
def portfolio_details():
    return render_template('portfolio_details.html')

@app.route("/single-blog")
def single_blog():
    return render_template('single-blog.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        contacts_name = request.form.get("name")
        contacts_email = request.form.get("email")
        contacts_message = request.form.get("message")
        contacts_subject = request.form.get("subject")

        #print(contacts_name)
        #print(contacts_email)
        #print(contacts_message)

        #return render_template("success.html")


@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['name'] != 'd1m0n' or request.form['password'] != 'pass123':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)