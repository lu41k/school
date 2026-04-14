from flask import Flask, render_template
from database import Database


app = Flask(__name__)
db = Database()


@app.route("/")
def welcome_func():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def registration():
    return render_template("register.html")


@app.route("/add-user")
def adding_user():
    return "ok"


if __name__ == "__main__":
    app.run(port=8000)
