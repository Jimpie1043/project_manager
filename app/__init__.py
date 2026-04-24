import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

from app.utils.security import init_security

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app(test_config=None):
    load_dotenv()
    
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
    SECRET_KEY=os.getenv("SECRET_KEY"),
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'app.db')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG=os.getenv("FLASK_DEBUG") == "1"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    os.makedirs(app.instance_path, exist_ok=True)

    init_security(app)
    csrf.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import workspace
    app.register_blueprint(workspace.bp)
    app.add_url_rule('/', endpoint='index')

    return app