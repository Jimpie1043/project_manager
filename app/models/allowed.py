from app import db

class Allowed(db.Model):
    __tablename__ = 'allowed_table'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    user_id = db.column(db.Integer, nullable=False)
    role = db.Column(db.String(50), nullable=False)