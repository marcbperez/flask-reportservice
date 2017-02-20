from ..database import db
from sqlalchemy.dialects.postgresql import JSON


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(JSON)
