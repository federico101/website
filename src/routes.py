from flask import redirect, render_template, url_for, flash

from src import app
from src.forms import LoginForm, RegistrationForm


class Box:
    def __init__(self, name, description=None, redirect=None) -> None:
        self.name = name

        if description is None:
            description = f"{name} related stuff"
        self.description = description

        if redirect is None:
            redirect = self.name.lower()
        self.redirect = redirect


BOXES = [
    Box("Portfolio"),
    Box("Contacts"),
    Box("Game"),
    Box("Services"),
    Box("Login"),
    Box("Register"),
]


@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", boxes=BOXES)


@app.route("/login/", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "test@test.com" and form.password.data == "password":
            flash("You have logged in!")
            return redirect(url_for("home"))
        else:
            flash("incorrect data!")

    return render_template("login.html", form=form)


@app.route("/logout/")
def logout():
    return render_template("home.html", boxes=BOXES)


@app.route("/register/", methods=["POST", "GET"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash("You have registered in!")
        return redirect(url_for("home"))

    return render_template("register.html", form=form)


@app.route("/account/")
def account():
    return render_template("home.html", boxes=BOXES)


@app.route("/admin/")
def admin():
    return render_template("home.html", boxes=BOXES)


@app.route("/about/")
def about():
    return render_template("home.html", boxes=BOXES)


@app.route("/contacts/")
def contacts():
    return render_template("home.html", boxes=BOXES)


@app.route("/game/")
def game():
    return render_template("home.html", boxes=BOXES)


@app.route("/portfolio/")
def portfolio():
    return render_template("home.html", boxes=BOXES)


@app.route("/portfolio/projects/")
def projects():
    return render_template("home.html", boxes=BOXES)


@app.route("/services/")
def services():
    return render_template("home.html", boxes=BOXES)


@app.route("/services/bots/")
def bots():
    return render_template("home.html", boxes=BOXES)


@app.route("/services/websites/")
def websites():
    return render_template("home.html", boxes=BOXES)
