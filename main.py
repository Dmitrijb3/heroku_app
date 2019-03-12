from flask import Flask, render_template, request
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

@app.route("/sign_up")
def sign_up():
    return render_template('sign_up.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    cookie_name = request.cookies.get("user_name") # Переделать !!!!
    contact_name = request.form.get("name")
    result = None
    if contact_name:
        print('No klienta atnaca: {}'.format(contact_name))
        result = contact_name.upper()
    return render_template('login.html', result=result, login_name=cookie_name)

if __name__ == '__main__':
    app.run(debug=True)