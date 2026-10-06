from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from database import Database
from hash_function import get_hash_password
from functools import wraps
import werkzeug.exceptions as exc


app = Flask(__name__)
db = Database()


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "email" not in session:
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)
    return wrapped_view


@app.route("/")
def welcome_func():
    if "email" in session:
        return redirect(url_for("profile"))

    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if "email" in session:
        return redirect(url_for("profile"))

    return render_template("login.html")


@app.route("/register")
def registration():
    if "email" in session:
        return redirect(url_for("profile"))

    return render_template("register.html")


@app.route("/profile")
@login_required
def profile():
    user = get_db().execute(
        "SELECT username, email FROM users WHERE id = ?",
        (session["user_id"],)
    ).fetchone()

    if user is None:
        session.clear()
        return redirect(url_for("login"))

    return render_template("profile.html", user=user)


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
    if "email" in session:
        return redirect(url_for("profile"))

    email = request.form.get("email")
    password = request.form.get("password")

    password_in_db = db.select_user_password(email=email)
    if not password_in_db:
        return jsonify({"error": "User not found"}), 404

    if get_hash_password(password) != password_in_db:
        return jsonify({"error": "Incorrect password"}), 401

    session.clear()
    session["user_id"] = email

    return redirect(url_for("profile"))


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
