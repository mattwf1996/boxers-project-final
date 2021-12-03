from application import db

class Division(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight_range = db.Column(db.String(30), nullable=False)
    boxers = db.relationship('Boxer', backref='division')
    #add weight range column
    

class Boxer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    boxer_name = db.Column(db.String(30), nullable=False)
    division_id = db.Column(db.Integer, db.ForeignKey('division.id'), nullable=False)
