from flask import (
    Blueprint, render_template, url_for, redirect, session
)

from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models import User
from app.utils.forms import SignupForm, LoginForm


auth = Blueprint('auth', __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = SignupForm()

    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            hashed_password=generate_password_hash(form.password.data),
            admin = False
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.hashed_password, form.password.data):
            session["user_id"] = user.id
            return redirect(url_for("workspace.index"))

        return "Invalid credentials"

    return render_template("auth/login.html", form=form)


@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))