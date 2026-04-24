from app import db

class Allowed(db.Model):
    __tablename__ = 'allowed_table'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project_table.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    user = db.relationship(
        "User",
        back_populates="allowed_projects"
        )
    
    project = db.relationship(
        "Project",
        back_populates="allowed_users"
        )