from flask import Flask, render_template, jsonify, request
from database import Database
from hash_function import get_hash_password


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


@app.route("/add-user", methods=["POST"])
def adding_user():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        db.add_user(name=name, email=email, password=get_hash_password(password=password))
    except:
        pass

    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
