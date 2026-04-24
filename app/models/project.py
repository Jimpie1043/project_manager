from app import db

class Allowed(db.Model):
    __tablename__ = 'project_table'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.column(db.Integer, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))