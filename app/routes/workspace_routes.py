from flask import (
    Blueprint, render_template, url_for, request, redirect, flash, session
)

from app import db
from app.models.project import Project
from app.models.allowed import Allowed
from app.utils.auth import login_required


workspace = Blueprint('workspace', __name__)


@workspace.route('/')
@login_required
def index():
    """
    WILL HAVE TO MAKE SURE YOU CAN ONLY SEE YOUR OWNED/ALLOWED PROJECTS
    """
    projects = Allowed.query.filter_by(user_id=session["user_id"]).all
    return render_template('workspace/index.html', projects=projects)


@workspace.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            new_project = Project(
                title=title,
                description=description
            )

            db.session.add(new_project)
            db.session.commit()

            return redirect(url_for('workspace.index'))
        

"""ROUTES TO ADD"""
@workspace.route('/<int:project_id>')
@login_required
def project():
    projects = Allowed.query.filter_by(user_id=session["user_id"]).all


@workspace.route('/<int:project_id>/edit')
@login_required
def project_edit():
    projects = Allowed.query.filter_by(user_id=session["user_id"]).all


@workspace.route('/<int:project_id>/delete')
@login_required
def project_delete():
    projects = Allowed.query.filter_by(user_id=session["user_id"]).all