from app import app, db
from app.models import User, CronicsIlness,Vision,MedicCheck,ArterialTension,Donor,Complementary, BodyExamn,Psicological,Incidents,Patiente,ExpositionRisks,GeneticsRisks,Vacunation, PahtolocalHistory,OcupationalHistory, InitialSanitaryControl, InitialHealthState, ChargeSheet, Resume

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Patiente': Patiente,
            'ChargeSheet': ChargeSheet, 'Resume': Resume,
            'OcupationalHistory': OcupationalHistory, 'InitialHealthState': InitialHealthState,
            'PahtolocalHistory': PahtolocalHistory, 'InitialSanitaryControl': InitialSanitaryControl,
            'Vacunation': Vacunation, 'GeneticsRisks': GeneticsRisks,
            'ExpositionRisks': ExpositionRisks, 'CronicsIlness': CronicsIlness,
            'Incidents': Incidents, 'Psicological': Psicological,
            'BodyExamn': BodyExamn, 'Complementary': Complementary,
            'ArterialTension': ArterialTension, 'Donor': Donor,
            'Vision': Vision, 'MedicCheck': MedicCheck}