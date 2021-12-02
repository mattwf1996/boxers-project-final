from application import db

class Division(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    division_name = db.Column(db.String(30), nullable=False)
    boxers = db.relationship('Boxer', backref='country')
    # completed = db.Column(db.Boolean, nullable=False, default=False)

class Boxer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    boxer_name = db.Column(db.String(30), nullable=False)
    boxers = db.relationship('Boxer')
    division_id = db.Column(db.Integer, db.ForeignKey('division_id'), nullable=False)
    # completed = db.Column(db.Boolean, nullable=False, default=False)