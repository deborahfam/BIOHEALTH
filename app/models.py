from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Patiente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.Integer, primary_key=True)
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
    chargesheet_id = db.relationship("ChargeSheet", backref= 'patiente', lazy = 'dynamic')
    resume_id = db.relationship("Resume", backref= 'patiente', lazy = 'dynamic')
    ocupatHist_id = db.relationship("OcupationalHistory", backref= 'patiente', lazy = 'dynamic')
    iniHealthState_id = db.relationship("InitialHealthState", backref= 'patiente', lazy = 'dynamic')
    pathologicalHistory_id = db.relationship("PathologicalHistory", backref= 'patiente', lazy = 'dynamic')
    initialSanitaryControl = db.relationship("InitialSanitaryControl", backref= 'patiente', lazy = 'dynamic')
    vacunation_id = db.relationship("Vacunation", backref= 'patiente', lazy = 'dynamic')
    geneticsRisks_id = db.relationship("GeneticsRisks", backref= 'patiente', lazy = 'dynamic')
    expositionRisks_id = db.relationship("ExpositionRisks", backref= 'patiente', lazy = 'dynamic')
    cronicsIlness_id = db.relationship("CronicsIlness", backref= 'patiente', lazy = 'dynamic')
    incidents_id = db.relationship("Incidents", backref= 'patiente', lazy = 'dynamic')
    psicological_id = db.relationship("Psicological", backref= 'patiente', lazy = 'dynamic')
    bodyExamn_id = db.relationship("BodyExamn", backref= 'patiente', lazy = 'dynamic')
    complementary_id = db.relationship("Complementary", backref= 'patiente', lazy = 'dynamic')
    arterialTension_id = db.relationship("ArterialTension", backref= 'patiente', lazy = 'dynamic')
    donor_id = db.relationship("Donor", backref= 'patiente', lazy = 'dynamic')
    vision_id = db.relationship("Vision", backref= 'patiente', lazy = 'dynamic')
    medicCheck_id = db.relationship("MedicCheck", backref= 'patiente', lazy = 'dynamic')
    
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
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)    
    dispensaryGroup = db.Column(db.String(64), index = True)
    valoration = db.Column(db.String(200), index = True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class OcupationalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)  
    previousOccupation = db.Column(db.String(64), index = True)
    exposedTo = db.Column(db.String(64), index = True)
    exposedToInTime = db.Column(db.String(64), index = True)
    currentOccupation = db.Column(db.String(64), index = True)
    currentOccupationSince = db.Column(db.Date, index = True)
    currentOccupationTo = db.Column(db.Date, index = True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class InitialHealthState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drugAlergy = db.Column(db.String(64), index = True)
    tetanusVaccionelastActivation = db.Column(db.Date, index=True)
    tetanusVaccionenextActivation = db.Column(db.Date, index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class PathologicalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pathologies = db.Column(db.String(20), index = True)
    othersPathologies = db.Column(db.String(64), index = True)
    professionalIlness = db.Column(db.String(64), index = True)
    surgeries = db.Column(db.String(64), index = True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

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
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class Vacunation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vaccines = db.Column(db.String(11), index = True)
    anothers = db.Column(db.String(64), index = True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class GeneticsRisks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    risks = db.Column(db.String(4), index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class ExpositionRisks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    risks = db.Column(db.String(17), index=True)
    anothers = db.Column(db.String(64), index=True)
    non_ionazinRadiations = db.Column(db.String(4), index=True)
    ionazingRadiations = db.Column(db.String(6), index=True)
    expRadiometricEvaluation = db.Column(db.String(1), index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    
    
class CronicsIlness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    ilness = db.Column(db.String(20), index=True)
    anothers = db.Column(db.String(64), index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

#UNFINISH
class Incidents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    casualEvent = db.Column(db.String(64), index=True)
    accident = db.Column(db.Boolean, index=True)
    accidentProperties = db.Column(db.String(64), index=True)
    medicalCerificated = db.Column(db.String(64), index=True)
    indicatedBy = db.Column(db.String(64), index=True)
    medicalCerificatedSince = db.Column(db.Date, index=True)
    medicalCerificatedTo = db.Column(db.Date, index=True)
    medicalcertificatedCauses = db.Column(db.String(64), index=True)
    medicalCertificatedFrom = db.Column(db.String(64), index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class Psicological(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    workFeelings = db.Column(db.String(64), index = True)
    stressLevel = db.Column(db.String(64), index = True)
    symptoms = db.Column(db.String(64), index = True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    
    
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
    cardiovasculary = db.Column(db.String(64), index=True)
    digestive = db.Column(db.String(64), index=True)
    rectal = db.Column(db.String(64), index=True)
    TAS = db.Column(db.Float, index=True)
    TAD = db.Column(db.Float, index=True)
    SArtPerfi = db.Column(db.String(64), index=True)
    SVenPerif = db.Column(db.String(64), index=True)
    hemalinfopoyetic = db.Column(db.String(64), index=True)
    genitourin_mas = db.Column(db.String(64), index=True)
    osteomioarticular = db.Column(db.String(64), index=True)
    scapularGirdleUperLimbs = db.Column(db.String(64), index=True)
    pelvicGirdleLowerLimbs = db.Column(db.String(64), index=True)
    spine = db.Column(db.String(64), index=True)
    neurologicStats = db.Column(db.String(64), index=True)    
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    
    
class Complementary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    Hb = db.Column(db.Float, index=True)
    Hto = db.Column(db.Float, index=True)
    Leuco = db.Column(db.Float, index=True)
    VSG = db.Column(db.Float, index=True)
    peripheralLamina = db.Column(db.String(64), index=True)
    HDL = db.Column(db.String(64), index=True)
    Glicemy = db.Column(db.String(64), index=True)
    Creatimia = db.Column(db.String(64), index=True)
    AcUrico = db.Column(db.String(64), index=True)
    LDH = db.Column(db.String(64), index=True)
    TGP = db.Column(db.String(64), index=True)
    TGO = db.Column(db.String(64), index=True)
    T4 = db.Column(db.String(64), index=True)
    colesterol = db.Column(db.String(64), index=True)
    triglicrids = db.Column(db.String(64), index=True)
    T3 = db.Column(db.String(64), index=True)
    TSH= db.Column(db.String(64), index=True)
    PSA= db.Column(db.String(64), index=True)
    colinesterasa= db.Column(db.String(64), index=True)
    plomo= db.Column(db.String(64), index=True)
    corpocultivo= db.Column(db.String(64), index=True)
    exudados= db.Column(db.String(64), index=True)
    fecalHeces= db.Column(db.String(64), index=True)
    VIH= db.Column(db.String(64), index=True)
    VIHDate= db.Column(db.Date, index=True)
    VIHResult= db.Column(db.Boolean, index=True)
    Sifilis= db.Column(db.String(64), index=True)
    SifilisDate= db.Column(db.Date, index=True)
    SifilisResult= db.Column(db.Boolean, index=True)
    BHepatitis= db.Column(db.String(64), index=True)
    BHepatitisDate= db.Column(db.Date, index=True)
    BHepatitisResult= db.Column(db.Boolean, index=True)
    CHepatitis= db.Column(db.String(64), index=True)
    CHepatitisDate= db.Column(db.Date, index=True)
    CHepatitisResult= db.Column(db.Boolean, index=True)
    adiometricaTest= db.Column(db.String(64), index=True)
    Rx= db.Column(db.String(64), index=True)
    EKG= db.Column(db.String(64), index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    
   
class ArterialTension(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    TAS= db.Column(db.Float, index=True)
    TDH= db.Column(db.Float, index=True)
    position= db.Column(db.String(64), index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    
   
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class Vision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    evaluationCenter= db.Column(db.String(64), index=True)
    OD= db.Column(db.String(64), index=True)
    OI= db.Column(db.String(64), index=True)
    results= db.Column(db.String(64), index=True)
    diagnostic= db.Column(db.String(64), index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    

class MedicCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index = True)
    pathologicalInterest= db.Column(db.String(64), index=True)
    laboralInterestRisks= db.Column(db.String(64), index=True)
    correctivesActions= db.Column(db.String(64), index=True)
    individualProtection= db.Column(db.String(64), index=True)
    nutricionalEvaluation= db.Column(db.String(64), index=True)
    complementaryResume= db.Column(db.String(64), index=True)
    bodyStateResume= db.Column(db.String(64), index=True)
    DispensarialResume= db.Column(db.String(64), index=True)
    extra= db.Column(db.String(64), index=True)
    suitable= db.Column(db.String(64), index=True)
    correctiveAction= db.Column(db.String(64), index=True)
    nextMedicCheck = db.Column(db.Date, index=True)
    check= db.Column(db.Boolean, index=True)
    patiente_id = db.Column(db.Integer, db.ForeignKey('patiente.ci'))
    
