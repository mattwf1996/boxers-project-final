from application import db

class Boxers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(30), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)