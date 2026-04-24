import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from flask_babel import Babel

from app.utils.security import init_security
from app.config import Config


# Assign extensions
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
babel = Babel()

def create_app(test_config=None):
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///{os.path.join(app.instance_path, 'app.db')}"
    )

    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)

    init_security(app)

    from .routes.auth_routes import auth
    from .routes.workspace_routes import workspace

    app.register_blueprint(auth)
    app.register_blueprint(workspace)

    return app