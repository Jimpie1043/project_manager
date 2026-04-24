from app import db

class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    projects = db.relationship(
        "Project",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan")