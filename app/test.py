from app import db
from app.models import *

# Crear elementos de prueba
patiente1 = Patiente(ci=12345678, down=False, jobRecord=1234, jobZone='Construction', ocupCategory='Construction Worker', date='2022-12-22', firstname='John', lastname='Doe', age=35, sex='M', skinColor='B', educLevel='High School', cellphone='1234567890', street='Main Street', between='1st and 2nd Ave', neighborhood='Downtown', number=123, apt_number=None, province='New York', municipality='New York City', edadGroup=3, factorGroup=2, donor=True)
patiente2 = Patiente(ci=87654321, down=True, jobRecord=4321, jobZone='Education', ocupCategory='Teacher', date='2022-12-22', firstname='Jane', lastname='Smith', age=28, sex='F', skinColor='W', educLevel='Bachelors Degree', cellphone='0987654321', street='Maple Street', between='2nd and 3rd Ave', neighborhood='Suburb', number=456, apt_number=7, province='California', municipality='Los Angeles', edadGroup=2, factorGroup=3, donor=False)

chargeSheet1 = ChargeSheet(date='2022-12-22', consultationReason='Sore throat', diagnostic='Pharyngitis', reaction='None', indicatedDrugs='Ibuprofen, Paracetamol', evolution='Improved after 2 days of treatment', patiente_id=12345678)
chargeSheet2 = ChargeSheet(date='2022-12-23', consultationReason='Fever', diagnostic='Influenza', reaction='None', indicatedDrugs='Tamiflu', evolution='Recovered after 5 days of treatment', patiente_id=87654321)

resume1 = Resume(date='2022-12-22', dispensaryGroup='Primary Care', valoration='Patient is in good health', patiente_id=12345678)
resume2 = Resume(date='2022-12-23', dispensaryGroup='Primary Care', valoration='Patient has a history of asthma, currently well-controlled with medication', patiente_id=87654321)

ocupationalHistory1 = OcupationalHistory(date='2022-12-22', previousOccupation='Construction Worker', exposedTo='Asbestos', exposedToInTime='5 years', currentOccupation='Teacher', currentOccupationSince='2020-01-01', currentOccupationTo=None, patiente_id=12345678)
ocupationalHistory2 = OcupationalHistory(date='2022-12-23', previousOccupation='Teacher', exposedTo='None', exposedToInTime='None', currentOccupation='Office Worker', currentOccupationSince='2019-01-01', currentOccupationTo=None, patiente_id=87654321)

initialHealthState1 = InitialHealthState(drugAlergy='None', tetanusVaccionelastActivation='2020-01-01', tetanusVaccionenextActivation='2023-01-01', patiente_id=12345678)
initialHealthState2 = InitialHealthState(drugAlergy='Penicillin', tetanusVaccionelastActivation='2018-01-01', tetanusVaccionenextActivation='2023-01-01', patiente_id=87654321)

pathologicalHistory1 = PathologicalHistory(pathologies='None', othersPathologies='None', professionalIlness='None', surgeries='None', patiente_id=12345678)
pathologicalHistory2 = PathologicalHistory(pathologies='Hypertension', othersPathologies='None', professionalIlness='None', surgeries='None', patiente_id=87654321)

initialSanitaryControl1 = InitialSanitaryControl(country='Mexico', outside=True, departureDate='2022-01-01', arrivalDate='2022-01-07', returnControl=True, returnControlDate='2022-02-01', controls='All clear', return3MonthControl=True, returneMothControlDate='2022-05-01', controls3Month='All clear', patiente_id=12345678)
initialSanitaryControl2 = InitialSanitaryControl(country='Japan', outside=True, departureDate='2022-02-15', arrivalDate='2022-02-22', returnControl=True, returnControlDate='2022-03-15', controls='All clear', return3MonthControl=False, returneMothControlDate=None, controls3Month='None', patiente_id=87654321)

vacunation1 = Vacunation(vaccines='Influenza', anothers='None', patiente_id=12345678)
vacunation2 = Vacunation(vaccines='HPV', anothers='None', patiente_id=87654321)

geneticsRisks1 = GeneticsRisks(date='2022-12-22', risks='None', patiente_id=12345678)
geneticsRisks2 = GeneticsRisks(date='2022-12-23', risks='None', patiente_id=87654321)

expositionRisks1 = ExpositionRisks(date="2022-01-01", risks="Riesgos de exposición", patiente=patiente1)
expositionRisks2 = ExpositionRisks(date="2022-01-01", risks="Riesgos de exposición", patiente=patiente2)

cronicsIllness1 = CronicsIlness(date="2022-01-01", ilness="Enfermedad crónica", patiente=patiente1)
cronicsIllness2 = CronicsIlness(date="2022-01-01", ilness="Enfermedad crónica", patiente=patiente2)

incidents1 = Incidents(date="2022-01-01", casualEvent="Evento casual", patiente=patiente1)
incidents2 = Incidents(date="2022-01-01", casualEvent="Evento casual", patiente=patiente2)

psicological1 = Psicological(date="2022-01-01", workFeelings="Sentimientos en el trabajo", patiente=patiente1)
psicological2 = Psicological(date="2022-01-01", workFeelings="Sentimientos en el trabajo", patiente=patiente2)

bodyExamn1 = BodyExamn(date="2022-01-01", kgWeight=75.5, sizeInM=1.75, patiente=patiente1)
bodyExamn2 = BodyExamn(date="2022-01-01", kgWeight=80.0, sizeInM=1.80, patiente=patiente2)

complementary1 = Complementary(date="2022-01-01", Hb=12.0, patiente=patiente1)
complementary2 = Complementary(date="2022-01-01", Hb=13.0, patiente=patiente2)

arterialTension1 = ArterialTension(date="2022-01-01", TAS=120, TDH=80, patiente=patiente1)
arterialTension2 = ArterialTension(date="2022-01-01", TAS=110, TDH=70, patiente=patiente2)

donor1 = Donor(date="2022-01-01", patiente=patiente1)
donor2 = Donor(date="2022-01-01", patiente=patiente2)

vision1 = Vision(date="2022-01-01", evaluationCenter="Centro de evaluación", patiente=patiente1)
vision2 = Vision(date="2022-01-01", evaluationCenter="Centro de evaluación", patiente=patiente2)

medicCheck1 = MedicCheck(date="2022-01-01", pathologicalInterest="Intereses patológicos", patiente=patiente1)
medicCheck2 = MedicCheck(date="2022-01-01", pathologicalInterest="Intereses patológicos", patiente=patiente2)

#Añadir elementos de prueba a la base de datos
db.session.add(patiente1)
db.session.add(patiente2)
db.session.add(expositionRisks1)
db.session.add(expositionRisks2)
db.session.add(cronicsIllness1)
db.session.add(cronicsIllness2)
db.session.add(incidents1)
db.session.add(incidents2)
db.session.add(psicological1)
db.session.add(psicological2)
db.session.add(bodyExamn1)
db.session.add(bodyExamn2)
db.session.add(complementary1)
db.session.add(complementary2)
db.session.add(arterialTension1)
db.session.add(arterialTension2)
db.session.add(donor1)
db.session.add(donor2)
db.session.add(vision1)
db.session.add(vision2)
db.session.add(medicCheck1)
db.session.add(medicCheck2)

#Guardar los cambios en la base de datos
db.session.commit()

#Mostrar el contenido de la tabla Patiente
print("Contenido de la tabla Patiente:")
print(Patiente.query.all())

#Mostrar el contenido de la tabla ExpositionRisks
print("Contenido de la tabla ExpositionRisks:")
print(ExpositionRisks.query.all())

#Mostrar el contenido de la tabla CronicsIllness
print("Contenido de la tabla CronicsIllness:")
print(CronicsIlness.query.all())

#Mostrar el contenido de la tabla Incidents
print("Contenido de la tabla Incidents:")
print(Incidents.query.all())

#Mostrar el contenido de la tabla Psicological
print("Contenido de la tabla Psicological:")
print(Psicological.query.all())

#Mostrar el contenido de la tabla BodyExamn
print("Contenido de la tabla BodyExamn:")
print(BodyExamn.query.all())

#Mostrar el contenido de la tabla Complementary
print("Contenido de la tabla Complementary:")
print(Complementary.query.all())

#Mostrar el contenido de la tabla ArterialTension
print("Contenido de la tabla ArterialTension:")
print(ArterialTension.query.all())

#Mostrar el contenido de la tabla Donor
print("Contenido de la tabla Donor:")
print(Donor.query.all())

#Mostrar el contenido de la tabla Vision
print("Contenido de la tabla Vision:")
print(Vision.query.all())

#Mostrar el contenido de la tabla MedicCheck
print("Contenido de la tabla MedicCheck:")
print(MedicCheck.query.all())
