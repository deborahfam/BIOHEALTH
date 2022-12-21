from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Patiente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    down = db.Column(db.Boolean, index=True)
    jobRecord = db.Column(db.Integer, index=True)
    jobZone = db.Column(db.String(64), index=True)
    ocupCategory = db.Column(db.String(64), index=True)
    fecha = db.Column(db.Date, index=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    sex = db.Column(db.String(1), index=True)
    skinColor = db.Column(db.String(1), index=True)
    educLevel = db.Column(db.String(64), index=True)
    cellphone = db.Column(db.String(12), index=True)
    street = db.Column(db.String(64), index=True)
    between = db.Column(db.String(64), index=True)
    neighborhood = db.Column(db.String(64), index=True)
    number = db.Column(db.Integer, index=True)
    apt_number = db.Column(db.Integer, index=True)    
    province = db.Column(db.String(64), index=True)
    minicipality = db.Column(db.String(64), index=True)
    edadGroup = db.Column(db.Integer, index=True)
    factorGroup = db.Column(db.Integer, index=True)
    donor = db.Column(db.Boolean, index=True)
    
    def __repr__(self):
        return '<Patiente {}>'.format(self.firstname + self.lastname)