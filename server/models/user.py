from __init__ import db
from flask_sqlalchemy import SQLAlchemy

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'id' : self.id,
            'first_name' : self.first_name,
            'last_name' : self.last_name
        }
