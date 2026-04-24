from flask import (
    Blueprint, render_template, url_for, request, redirect, flash
)

from app import db


auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    return


@auth.route('/login')
def login():
    return


@auth.route('/logout')
def logout():
    return