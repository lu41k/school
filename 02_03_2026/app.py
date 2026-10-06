from flask import Flask, render_template, jsonify, request
from database import Database
from hash_function import get_hash_password
import werkzeug.exceptions as exc


app = Flask(__name__)
db = Database()


@app.route("/")
def welcome_func():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
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

    if not db.select_user(email=email):
        try:
            db.add_user(name=name, email=email, password=get_hash_password(password=password))

            return render_template("index.html")

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "User with this email already exists"}), 400


@app.route("/login-user", methods=["POST"])
def log_in_user():
    email = request.form.get("email")
    password = request.form.get("password")

    password_in_db = db.select_user_password(email=email)
    if not password_in_db:
        return jsonify({"error": "User not found"}), 404

    if get_hash_password(password) != password_in_db:
        return jsonify({"error": "Incorrect password"}), 401

    return render_template("index.html")


@app.errorhandler(exc.HTTPException)
def handle_http_exception(e):
    return jsonify({
        "status": e.status_code,
        "message": e.description
    }), e.status_code


@app.errorhandler(Exception)
def handle_internal_error(e):
    return jsonify({
        "status": 500,
        "message": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(port=8000, debug=True)
