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
    date = db.Column(db.Date, index=True)
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

class ChargeSheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    consultationReason = db.Column(db.String(64), index = True)
    diagnostic = db.Column(db.String(64), index = True)
    reaction = db.Column(db.String(64), index = True)
    indicatedDrugs = db.Column(db.String(64), index = True)
    evolution = db.Column(db.String(200), index = True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)    
    dispensaryGroup = db.Column(db.String(64), index = True)
    valoration = db.Column(db.String(200), index = True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class OcupationalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)  
    previousOccupation = db.Column(db.String(64), index = True)
    exposedTo = db.Column(db.String(64), index = True)
    exposedToInTime = db.Column(db.String(64), index = True)
    currentOccupation = db.Column(db.String(64), index = True)
    currentOccupationSince = db.Column(db.Date, index = True)
    currentOccupationTo = db.Column(db.Date, index = True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class InitialHealthState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drugAlergy = db.Column(db.String(64), index = True)
    tetanusVaccionelastActivation = db.Column(db.Date, index=True)
    tetanusVaccionenextActivation = db.Column(db.Date, index=True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class PahtolocalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pathologies = db.Column(db.String(20), index = True)
    othersPathologies = db.Column(db.String(64), index = True)
    professionalIlness = db.Column(db.String(64), index = True)
    surgeries = db.Column(db.String(64), index = True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class InitialSanitaryControl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64), index = True)
    outside = db.Column(db.Boolean, index = True)
    departureDate = db.Column(db.Date, index = True)
    arrivalDate = db.Column(db.Date, index = True)
    returnControl = db.Column(db.Boolean, index = True)
    returnControlDate = db.Column(db.Date, index = True)
    controls = db.Column(db.String(6), index = True)
    return3MonthControl = db.Column(db.Boolean, index = True)
    returneMothControlDate = db.Column(db.Date, index = True)
    controls3Month = db.Column(db.String(6), index = True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class Vacunation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vaccines = db.Column(db.String(11), index = True)
    anothers = db.Column(db.String(64), index = True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class GeneticsRisks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    risks = db.Column(db.String(4), index=True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

class ExpositionRisks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    risks = db.Column(db.String(17), index=True)
    anothers = db.Column(db.String(64), index=True)
    non_ionazinRadiations = db.Column(db.String(4), index=True)
    ionazingRadiations = db.Column(db.String(6), index=True)
    expRadiometricEvaluation = db.Column(db.String(1), index=True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))
    
class CronicsIlness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    ilness = db.Column(db.String(20), index=True)
    anothers = db.Column(db.String(64), index=True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))

#UNFINISH
class Incidents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    casualEvent = db.Column(db.String(64), index=True)
    accident = db.Column(db.Boolean, index=True)
    accidentProperties = db.Column(db.String(64), index=True)

class Psicological(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    workFeelings = db.Column(db.String(64), index = True)
    stressLevel = db.Column(db.String(64), index = True)
    symptoms = db.Column(db.String(64), index = True)
    patiente = db.Column(db.Integer, db.ForeignKey('patiente.id'))
    patiente = db.relationship("Patiente", backref= db.backref("patiente", uselist=False))
    
class BodyExamn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    kgWeight = db.Column(db.Float, index=True)
    sizeInM = db.Column(db.Float, index=True)
    IMC = db.Column(db.Float, index=True)
    general = db.Column(db.String(64), index=True)
    regional = db.Column(db.String(64), index=True)
    thyroid = db.Column(db.String(64), index=True)
    brest = db.Column(db.String(64), index=True)
    interrrogation = db.Column(db.String(64), index=True)
    respiratory = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    nutricionalState = db.Column(db.String(64), index=True)
    
    