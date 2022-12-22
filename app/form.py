from flask_wtf import FlaskForm
from .constants import *
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, IntegerField, SelectMultipleField, widgets
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
    
    string_of_files = ['one', 'two', 'three']
    # create a list of value/description tuples
    files = [(x, x) for x in string_of_files]
    pathologies = MultiCheckboxField('Pathologies', choices=files)
    
    othersPathologies = StringField('Otras', validators=[DataRequired()])
    professionalIlness = StringField('Enfermedad Profesional', validators=[DataRequired()])
    surgeries = StringField('Cirugias Aplicadas', validators=[DataRequired()])
    submit = SubmitField('Crear Entrada')
    

class InitialSanitaryControlForm(FlaskForm):
    ci = StringField('CI', validators=[DataRequired()])
    country = SelectField('Tipo de Sangre', choices=[(x,x) for x in COUNTRIES])
    outside = BooleanField('Ha salido al extranjero')
    departureDate = DateField('Fecha de Salida', format='%d,%m,%Y')
    arrivalDate = DateField('Fecha de Salida', format='%d,%m,%Y')
    returnControl = BooleanField('Controlado al regreso')
    returnControlDate = DateField('Fecha de Control', format='%d,%m,%Y')
    ##missing controles realizados
    return3MonthControl = BooleanField('Controlado a los 3 Meses')
    returneMothControlDate = DateField('Fecha de Control', format='%d,%m,%Y')
    ##missing controles realizados

