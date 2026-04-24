from app import db

class Project(db.Model):
    __tablename__ = 'project_table'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))

    owner = db.relationship(
        "User",
        back_populates="owned_projects"
        )
    
    allowed_users = db.relationship(
        "Allowed",
        back_populates="project",
        cascade="all, delete-orphan"
        )
