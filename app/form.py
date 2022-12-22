from flask_wtf import FlaskForm
from .constants import *
from wtforms import StringField, PasswordField, FloatField, BooleanField, SubmitField, DateField, SelectField, IntegerField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class PatienteForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    jobRecord = StringField('Expediente Laboral', validators=[DataRequired()])
    firstName = StringField('Nombre', validators=[DataRequired()])
    lastName = StringField('Apellidos', validators=[DataRequired()])
    out = BooleanField('Baja')
    date = DateField('Fecha de Alta', format='%d/%m/%Y')
    o_category = SelectField('Categoria', choices=[(x, x) for x in OCUP_CATEGORY])
    area = SelectField("Area", choices=[(x,x) for x in AREAS_USER_FORM])
    age = IntegerField('Edad', validators=[DataRequired(),NumberRange(min=1,max=130)])
    sex = SelectField('Sexo', choices=[('M', 'M'), ('F', 'F')])
    study_level = SelectField('Nivel Educacional', choices=[('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA'), ('SUPERIOR', 'SUPERIOR')])
    color_skin = SelectField('Color de Piel', choices=[('BLANCO', 'BLANCO'), ('MESTIZO', 'MESTIZO'), ('NEGRO','NEGRO')])
    tel = StringField('Telefono')
    street = StringField('Calle')
    number = StringField('Numero')
    apt = StringField('Apartamento')
    between = StringField('Entrecalle')
    neighborhood = StringField('Barrio')
    province = SelectField('Provincia', choices=[(x["nombre"],x["nombre"]) for x in CUBA_INFO])
    municipality = SelectField('Municipio', choices=[(x,x) for x in CUBA_MUNICIPALITIES])
    ageGroup = StringField('Grupo Etario')
    bloodType = SelectField('Tipo de Sangre', choices=[(x,x) for x in BLOOD_TYPE])
    donor = BooleanField('Donante')
    submit = SubmitField('Crear Entrada')

class ChargesheetForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    date = DateField('Fecha', format='%d/%m/%Y')
    consultationReason = StringField('Motivo de Consulta', validators=[DataRequired()])
    diagnostic = StringField('Diagnostico', validators=[DataRequired()])
    reaction = StringField('Conducta', validators=[DataRequired()])
    indicatedDrugs = StringField('Farmacos indicados', validators=[DataRequired()])
    evolution = StringField('Evolucion', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class ResumeForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    anno = DateField('Anno', format='%d/%m/%Y')
    dispensaryGroup = SelectField('Grupo Dispensarial', choices=[(x,x) for x in DISPENSARIAL_GROUP])
    valoration = StringField('Valoracion', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')
    
#Not Working, don't know
class OcupationalHistoryForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    date = DateField('Fecha', format='%d/%m/%Y')
    previousOccupation = StringField('Labor Realizada', validators=[DataRequired()])
    exposedTo = StringField('Expuesto a', validators=[DataRequired()])
    exposedToInTime = StringField('Cuanto Tiempo', validators=[DataRequired()])
    currentOccupation = StringField('Ocupacion Actual', validators=[DataRequired()])
    currentOccupationSince = DateField('Desde', format='%d/%m/%Y')
    currentOccupationTo = DateField('Hasta', format='%d/%m/%Y')
    submit = SubmitField('Crear Entrada')
class InitialHealthStateForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    date = DateField('Fecha', format='%d/%m/%Y')
    drugAlergy = StringField('Alergia a Medicamentos', validators=[DataRequired()])
    tetanusVaccionelastActivation = DateField('Fecha ultima activacion', format='%d/%m/%Y')
    tetanusVaccionenextActivation = DateField('Fecha proxima activacion', format='%d/%m/%Y')
    submit = SubmitField('Crear Entrada')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
class PathologicalHistoryForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    
    string_of_files = [
        'Sarampión', 'Tuberculosis', 
        'Rubéola','Parotiditis',
        'Varicela','Leptospirosis',
        'Fiebre Tifoidea','Hepatitis Viral',
        'Dengue','Lepra', 'Paludismo',
        'Encefalitis Meningitis','Sifilis',
        'Gonorrea','Condiloma Acuminata',
        'Orquiepididimitis','Sindrome de Secrecion Uretal',
        'Enfermedad Inflamatoria Pelvia',
        'Sindrome de Secrecion Vaginal','Herpes Simple Genital'
        ]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files]
    pathologies = MultiCheckboxField('Pathologies', choices=files)
    
    othersPathologies = StringField('Otras', validators=[DataRequired()])
    professionalIlness = StringField('Enfermedad Profesional', validators=[DataRequired()])
    surgeries = StringField('Cirugias Aplicadas', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')
    

class InitialSanitaryControlForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    country = SelectField('País', choices=[(x,x) for x in COUNTRIES])
    outside = BooleanField('Ha salido al extranjero')
    departureDate = DateField('Fecha de Salida', format='%d,%m,%Y')
    arrivalDate = DateField('Fecha de Salida', format='%d,%m,%Y')
    returnControl = BooleanField('Controlado al regreso')
    returnControlDate = DateField('Fecha de Control', format='%d,%m,%Y')
    string_of_files1 = [
        'ELISA VIH', 'Gota Gruesa', 
        'Serología Sífilis','Serología Hepatitis B',
        'Serología Hepatitis C'
        ]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files1]
    controls = MultiCheckboxField('Controles realizados', choices=files)
    return3MonthControl = BooleanField('Controlado a los 3 Meses')
    returneMothControlDate = DateField('Fecha de Control', format='%d,%m,%Y')
    string_of_files2 = [
        'ELISA VIH', 'Gota Gruesa', 
        'Serología Sífilis','Serología Hepatitis B',
        'Serología Hepatitis C'
        ]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files2]
    controls3month = MultiCheckboxField('Controles realizados', choices=files)
    submit = SubmitField('Crear Entrada')
    
#TODO: Implementar los routes de las clases siguientes:
class VacunationForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    string_of_files = [
        'BCG', 'DPT', 'Anti-Polio',
        'PRS','Hepatitis B', 'Anti-Meningococo',
        'Anti-Leptospira','Anti-Tífica',
        'Anti-Influeza','Anti-rábica',
        'Anti-fiebre amarilla'
        ]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files]
    vaccines = MultiCheckboxField('Vacunas', choices=files)
    anothers = StringField('Otras', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')
    
class GeneticsRisksForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    date = DateField('Fecha', format='%d/%m/%Y')
    string_of_files = [
        'Cigarro', 'Alcohol', 'Obesidad',
        'Sedentarismo'
        ]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files]
    risks = MultiCheckboxField('Riesgos Geneticos', choices=files)

#Revisar ademas correctitud de los formularios
class ExpositionRisksForm(FlaskForm):
    date = DateField('Fecha de Exposición', format='%d/%m/%Y', validators=[DataRequired()])
    string_of_files1 = ['ruido', 'vibraciones', 
        'mala iluminacion', 'mala ventilacion', 'electricidad',
        'altas-bajas temperaturas',    'gases toxicos', 'acido',
        'caustico',    'posturas anormales', 'esfuerzo repetitivo',
        'agentes biológicos',    'suelo resbaladizo', 
        'mordeduras picadas', 'pvdatos'
        ]

    string_of_files_titled = [x.title() for x in string_of_files1]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files1]
    risks = MultiCheckboxField('Riesgos', choices=files)
    
    anothers = StringField('Otros', validators=[DataRequired()])
    
    string_of_files2 = ['ultravioleta', 'infrarroja', 
                        'campos eletromag/radiofrec', 'laser'
                       ]

    string_of_files_titled = [x.title() for x in string_of_files2]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files2]
    non_ionizingRadiations = MultiCheckboxField('Radiaciones No Ionizantes', choices=files)
    
    string_of_files3 = ['radio diagnóstico', 'radio terapia', 
        'medicina nuclear',    'radio inmunoensayo', 'industria'
        ]

    string_of_files_titled = [x.title() for x in string_of_files3]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files3]
    ionizingRadiations = MultiCheckboxField('Radiaciones Ionizantes', choices=files)
    
    expRadiometricEvaluation = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in RADIOMET])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class CronicsIlnessForm(FlaskForm):
    date = DateField('Fecha de Aparición', format='%d/%m/%Y', validators=[DataRequired()])
    
    string_of_files1 = ['ruido', 'vibraciones', 
        'mala iluminacion', 'mala ventilacion', 'electricidad',
        'altas-bajas temperaturas',    'gases toxicos', 'acido',
        'caustico',    'posturas anormales', 'esfuerzo repetitivo',
        'agentes biológicos',    'suelo resbaladizo', 
        'mordeduras picadas', 'pvdatos'
        ]

    string_of_files_titled = [x.title() for x in string_of_files1]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files1]
    illness = MultiCheckboxField('Enfermedades Cronicas', choices=files)
    
    anothers = StringField('Otros', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class IncidentsForm(FlaskForm):
    date = DateField('Fecha del Incidente', format='%d/%m/%Y', validators=[DataRequired()])
    casualEvent = StringField('Evento Casual', validators=[DataRequired()])
    accident = BooleanField('Accidente')
    
    string_of_files1 = ['comun', 'en el trayecto', 'en el trabajo',    
        'sin lesiones', 'con lesiones leves', 'con lesiones graves', 
        'muerte',    'con secuelas', 'esteticas', 'fisicas', 'psiquicas',  
        'con discapacidad', 'permantente', 'temporal', 'motoras'
        ]

    string_of_files_titled = [x.title() for x in string_of_files1]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files1]
    accidentProperties = MultiCheckboxField('Accidente', choices=files)
    
    medicalCerificated =SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Certificado Medico Inicial','Certificado medico Continuacion']])
    indicatedBy = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Medico del Centro','Medico de la Familia','Especialista']])
    medicalCerificatedSince = DateField('Desde Cuando tiene el Certificado Médico', format='%d/%m/%Y', validators=[DataRequired()])
    medicalCerificatedTo = DateField('Hasta Cuando tiene el Certificado Médico', format='%d/%m/%Y', validators=[DataRequired()])
    medicalCertificatedFrom = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Hospital','Cons Med Fam','Sala de Rehab','Cen S Mental','Hogar Materno']])
    
    string_of_files2 = ['riesgo obstetrico', 'lic prenatal', 'lic pos natal', 
        'accidente1', 'enfermedad comun'
        ]

    string_of_files_titled = [x.title() for x in string_of_files2]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files2]
    medicalcertificatedCauses = MultiCheckboxField('Causas', choices=files)
    
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class PsicologicalForm(FlaskForm):
    date = DateField('Fecha del Evaluación', format='%d/%m/%Y', validators=[DataRequired()])
    
    string_of_files2 = ['apoyado por su jefe', 'apoyado por su colectivo',
        'enajenado (aislado) por su jefe', 'enajenado (aislado) por su colectivo',
        'bien estimulado en relaciona su esfuerzo', 'hostigado por su jefe',
        'hostigado por su colectivo', 'bien estimulado por su relacion a su esfuerzo',
        'Motivado por sus tareas', 'Comprometido con sus metas', 
        'Con deseo de cambiar de puesto', 'Con deseo de cambiar de centro',
        'Protegido y seguro', 'Realizado y satisfecho'
        ]

    string_of_files_titled = [x.title() for x in string_of_files2]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files2]
    workFeelings = MultiCheckboxField('En el trabajo usted se siente', choices=files)
    
    string_of_files1 = [ 'Dificultad para dormir', 'Falta de concentración',
        'Se cansa facilmente',    'se entritece con fercuencia', 
        'tiene ronquidos fuertes y frecuentes mientras duerme',    
        'se despiera en la noche con ahogo por los ronquidos', 
        'se despierta por pesadillas',    
        'se ha dormido manejando leyendo o realizando sus labores', 
        'ansiedad',    'irritabilidad', 'fatigas frecuentes', 'palpitaicones',   
        'variacion en la capacidad de trabajo', 'cefalea', 'falta de aire',    
        'dolores corporales', 'arritmias cardiacas', 'necesidad de psicofarmacos'
        ]

    string_of_files_titled = [x.title() for x in string_of_files1]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files1]
    symptoms = MultiCheckboxField('Presenta alguno de los siguientes sintomas', choices=files)
    
    stressLevel = StringField('Nivel de Estrés', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class BodyExamnForm(FlaskForm):
    date = DateField('Fecha del Examen', format='%d/%m/%Y', validators=[DataRequired()])
    kgWeight = FloatField('Peso en Kg', validators=[DataRequired()])
    sizeInM = FloatField('Talla en M', validators=[DataRequired()])
    IMC = FloatField('IMC', validators=[DataRequired()])
    general = StringField('General', validators=[DataRequired()])
    regional = StringField('Regional', validators=[DataRequired()])
    thyroid = StringField('Tiroides', validators=[DataRequired()])
    brest = StringField('Mama', validators=[DataRequired()])
    interrrogation = StringField('Interrogatorio', validators=[DataRequired()])
    respiratory = StringField('Respiratorio', validators=[DataRequired()])
    cardiovasculary = StringField('Cardiovascular', validators=[DataRequired()])
    digestive = StringField('Digestivo', validators=[DataRequired()])
    rectal = StringField('Rectal', validators=[DataRequired()])
    TAS = FloatField('TAS', validators=[DataRequired()])
    TAD = FloatField('TAD', validators=[DataRequired()])
    SArtPerfi = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A']])
    SVenPerif = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A']])
    hemalinfopoyetic = StringField('Sistema Hematolinfopoyético', validators=[DataRequired()])
    genitourin_mas = StringField('Sistema Genitourinario y Mamas', validators=[DataRequired()])
    osteomioarticular =SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A']])
    scapularGirdleUperLimbs = StringField('Escapular y Cintura Escapular', validators=[DataRequired()])
    pelvicGirdleLowerLimbs = StringField('Cintura Pelvica y Miembros Inferiores', validators=[DataRequired()])
    spine = StringField('Columna Vertebral', validators=[DataRequired()])
    neurologicStats = StringField('Estado Neurológico', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class ComplementaryForm(FlaskForm):
    date = DateField('Fecha del Examen', format='%d/%m/%Y', validators=[DataRequired()])
    Hb = FloatField('Hb', validators=[DataRequired()])
    Hto = FloatField('Hto', validators=[DataRequired()])
    Leuco = FloatField('Leuco', validators=[DataRequired()])
    VSG = FloatField('VSG', validators=[DataRequired()])
    peripheralLamina = StringField('Laminillas Periféricas', validators=[DataRequired()])
    HDL = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Alta','Baja']])
    Glicemy = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Normal','De Riesgo','Elevada']])
    Creatimia = StringField('Creatinina', validators=[DataRequired()])
    AcUrico = StringField('Ácido Úrico', validators=[DataRequired()])
    LDH = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Normal','De Riesgo','Elevada']])
    TGP = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A','B']])
    TGO = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A','B']])
    T4 = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A','B']])
    colesterol = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Normal','De Riesgo','Elevada']])
    triglicrids = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Normal','De Riesgo','Elevada']])
    T3 = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A','B']])
    TSH = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A','B']])
    PSA = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['Normal','De Riesgo','Elevada']])
    colinesterasa = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A','B']])
    plomo = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','A','B']])
    corpocultivo = StringField('Corpocultivo', validators=[DataRequired()])
    exudados = StringField('Exudados', validators=[DataRequired()])
    fecalHeces = StringField('Heces Fecales', validators=[DataRequired()])
    VIH = StringField('VIH', validators=[DataRequired()])
    VIHDate = DateField('Fecha de Prueba VIH', format='%d/%m/%Y')
    VIHResult = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','P']])
    Sifilis = StringField('Sífilis', validators=[DataRequired()])
    SifilisDate = DateField('Fecha de Prueba de Sífilis', format='%d/%m/%Y')
    SifilisResult = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','P']])
    BHepatitis = StringField('Hepatitis B', validators=[DataRequired()])
    BHepatitisDate = DateField('Fecha de Prueba de Hepatitis B', format='%d/%m/%Y')
    BHepatitisResult = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','P']])
    CHepatitis = StringField('Hepatitis C', validators=[DataRequired()])
    CHepatitisDate = DateField('Fecha de Prueba de Hepatitis C', format='%d/%m/%Y')
    CHepatitisResult = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['N','P']])
    adiometricaTest = SelectField('Evaluacion Radiometrica de EXP', choices=[(x,x) for x in ['NORMAL','ALTERADA']])
    Rx = StringField('Rx', validators=[DataRequired()])
    EKG = StringField('EKG', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')
    
class ArterialTensionForm(FlaskForm):
    date = DateField('Fecha', format='%d/%m/%Y', validators=[DataRequired()])
    TAS = FloatField('TAS', validators=[DataRequired(), NumberRange(min=0)])
    TDH = FloatField('TDH', validators=[DataRequired(), NumberRange(min=0)])
    position = StringField('Posición', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class DonorForm(FlaskForm):
    date = DateField('Fecha', format='%d/%m/%Y', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class VisionForm(FlaskForm):
    date = DateField('Fecha', format='%d/%m/%Y', validators=[DataRequired()])
    evaluationCenter = StringField('Centro de Evaluación', validators=[DataRequired()])
    OD = FloatField('OD', validators=[DataRequired()])
    OI = FloatField('OI', validators=[DataRequired()])
    
    string_of_files1 = [ 'Normal', 'Requiere cristales o lente',
        'Cambi de cristales o lentes', 'Apto para el puesto', 
        'No apto para el puesto'
        ]

    string_of_files_titled = [x.title() for x in string_of_files1]
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files1]
    results = MultiCheckboxField('Resultados', choices=files)
    
    diagnostic = StringField('Diagnóstico', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

class MedicCheckForm(FlaskForm):
    date = DateField('Fecha', format='%d/%m/%Y', validators=[DataRequired()])
    pathologicalInterest = StringField('Interés Patológico', validators=[DataRequired()])
    laboralInterestRisks = StringField('Riesgos de Interés Laboral', validators=[DataRequired()])
    correctivesActions = StringField('Acciones Correctivas', validators=[DataRequired()])
    individualProtection = StringField('Protección Individual', validators=[DataRequired()])
    nutricionalEvaluation = StringField('Evaluación Nutricional', validators=[DataRequired()])
    complementaryResume = StringField('Resumen Complementario', validators=[DataRequired()])
    bodyStateResume = StringField('Resumen Estado Corporal', validators=[DataRequired()])
    DispensarialResume = StringField('Resumen Dispensarial', validators=[DataRequired()])
    extra = StringField('Extra', validators=[DataRequired()])
    suitable = StringField('Adecuado', validators=[DataRequired()])
    correctiveAction = StringField('Acciones Correctivas', validators=[DataRequired()])
    nextMedicCheck = DateField('Próximo Chequeo Médico', format='%d/%m/%Y', validators=[DataRequired()])
    check = BooleanField('Chequeo', validators=[DataRequired()])
    patiente_id = StringField('CI del Paciente', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')

