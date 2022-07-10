
from unicodedata import name
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.files import File
from app.models import *
from user.models import Patient, Doctor

from app.processing.get_data import *

class Command(BaseCommand):
    help = 'Upload data from Pandas dataFrames'

    def add_countries(self):
        self.stdout.write('Creating countries...\n\n')

        countries = [
            {
                'name': 'United States',
                'population': 329500000,
            },
            {
                'name': 'Colombia',
                'population': 50000000,
            },
            {
                'name': 'Unkkown',
                'population': None,
            },
        ]

        for country in countries:
            result = Country.objects.create(
                name=country['name'],
                population=country['population'],
            )
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def add_cities(self):
        self.stdout.write('\n\nCreating cities...\n\n')

        cities = [
            {
                'name': 'Bogotá',
                'country': Country.objects.filter(name='Colombia').first(),
                'population': 7000000,
            },
            {
                'name': 'Seatle',
                'country': Country.objects.filter(name='United States').first(),
                'population': None,
            },
            {
                'name': 'Austin',
                'country':  Country.objects.filter(name='United States').first(),
                'population': None, 
            },
            {
                'name': 'Medellín',
                'country': Country.objects.filter(name='Colombia').first(),
                'population': None, 
            },
            {
                'name': 'Unknown',
                'country': Country.objects.filter(name='Unknown').first(),
                'population': None, 
            },
        ]

        for city in cities:
            result = City.objects.create(
                name=city['name'],
                country=city['country'],
                population=city['population'],
            )
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def add_medical_areas(self):
        self.stdout.write('\n\nCreating areas...\n\n')
        medical_areas = [
            {
                'title': 'Pneumonia',
                'description': '',
            },
            {
                'title': 'Asthma',
                'description': '',
            },
            {
                'title': 'Bronchopulmonary',
                'description': '',
            },
            {
                'title': 'Respiratory Endoscopy',
                'description': '',
            },
        ]

        for area in medical_areas:
            result = MedicalArea.objects.create(
                title=area['title'],
                description=area['description'],
            )
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def add_patients(self):
        self.stdout.write('\n\nCreating patients...\n\n')

        for item in df_demographic.itertuples():
            patient = Patient.objects.create(
                first_name=item.first_name,
                last_name=item.last_name,
                legal_id=item.legal_id,
                email=item.email,
                age=item.Age,
                adult_bmi=item.Adult_BMI,
                sex=item.Sex,
                child_weight=item.Child_Weight,
                child_height=item.Child_Height,
            )
            patient.set_password('patient_123')
            patient.save()
            self.stdout.write(f'{patient} added.')
        self.stdout.write('-----')

    def add_doctors(self):
        self.stdout.write('\n\nCreating doctors...\n\n')

        doctors = [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'sex': 'M',
                'city': City.objects.get(name='Bogotá'),
                'legal_id': 123432,
                'email': 'd_001@doctor.com',
                'age': 34,
                
            },
            {
                'first_name': 'Jane',
                'last_name': 'Doe',
                'sex': 'F',
                'city': City.objects.get(name='Seatle'),
                'legal_id': 42234223,
                'email': 'd_002@doctor.com',
                'age': 30,
            },
            {
                'first_name': 'Julian',
                'last_name': 'Alzate',
                'sex': 'M',
                'city': City.objects.get(name='Bogotá'),
                'legal_id': 86439232,
                'email': 'd_003@doctor.com',
                'age': 45,
            },
            {
                'first_name': 'George',
                'last_name': 'Sears',
                'sex': 'M',
                'city': City.objects.get(name='Austin'),
                'legal_id': 77834234,
                'email': 'd_004@doctor.com',
                'age': 51,
            },
        ]
        
        for item in doctors:
            result = Doctor.objects.create(
                first_name=item['first_name'],
                last_name=item['last_name'],
                sex=item['sex'],
                city=item['city'],
                legal_id=item['legal_id'],
                email=item['email'],
                age=item['age'],
                is_staff=True,
            )
            result.medical_areas.add(
                *(MedicalArea.objects.all().order_by('?')[:3]),
            )
            result.set_password('doctor_123')
            result.save()
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def add_hospitals(self):
        self.stdout.write('\n\nCreating cities...\n\n')

        hospitals = [
            {
                'name': 'Hospital La Misericordia',
                'address': 'Calle falsa 123',
                'phone_number': 7563920,
                'legal_id': 9876543456,
                'city': City.objects.get(name='Bogotá'),
            },
            {
                'name': 'Seatle\'s hospital',
                'address': 'fake street 123',
                'phone_number': 7563921,
                'legal_id': 9876543454,
                'city': City.objects.get(name='Seatle'),
            },
        ]

        for hospital in hospitals:
            result = Hospital.objects.create(
                name=hospital['name'],
                address=hospital['address'],
                phone_number=hospital['phone_number'],
                legal_id=hospital['legal_id'],
                city=hospital['city'],
            )
            result.medical_areas.add(
                *(MedicalArea.objects.all().order_by('?')[:3]),
            ),
            len_patients = len(Patient.objects.all())
            result.patients.add(
                *(Patient.objects.all().order_by('?')[:len_patients//2]),
            ),
            result.doctors.add(
                *(Doctor.objects.all()),
            ),
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def add_medical_instruments(self):
        self.stdout.write('\n\nCreating instruments...\n\n')

        for category in df_annotation_info['Recording_equipment'].cat.categories:
            result = MedicalInstrument.objects.create(
                name=category,
            )
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def add_user_histories(self):
        self.stdout.write('\n\nCreating instruments...\n\n')

        for patient in Patient.objects.all():
            result = UserHistory.objects.create(
                patient=patient,
                doctor=Doctor.objects.all().order_by('?')[0],
            )
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')
            
    def add_audios(self):
        self.stdout.write('\n\nCreating and uploading audios...\n\n')

        for item in df_files.itertuples():
            result = Audio.objects.create(
                audio_filename=item.Audiofile_name,
                instrument=MedicalInstrument.objects.get(
                    name=item.Recording_equipment,
                ),
                city=City.objects.get(
                    name='Unknown',
                ),
                chest_location=item.Chest_location,
                mode=item.Acquisition_mode,
                # comments='',
                user_history=UserHistory.objects.get(
                    patient=Patient.objects.get(
                        first_name=str(item.Patient_number)
                    ),
                ),
                file=File(open(item.Audiofile_path, 'rb'), name=item.Audiofile_name + '.wav'),
            )
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def add_cycles(self):
        self.stdout.write('\n\nCreating cycles...\n\n')

        for item in df_total.itertuples():
            result = Cycle.objects.create(
                audio=Audio.objects.get(audio_filename=item.Audiofile_name),
                numestdo=item.Numestdo,
                begin_cycle=item.Begin_cycle,
                end_cycle=item.End_cycle,
                status=item.Status,
                variance=item.Variance,
                range_cycle=item.Range,
                sma_coarse=item.SMA_coarse,
                sma_fine=item.SMA_fine,
                avg_spectre=item.Spectre_AVG,
            )
            self.stdout.write(f'{result} added.')
        self.stdout.write('-----')

    def handle(self, *args, **kwargs):
        self.add_countries()
        self.add_cities()
        self.add_medical_areas()
        self.add_patients()
        self.add_doctors()
        self.add_hospitals()
        self.add_medical_instruments()
        self.add_user_histories()
        self.add_audios()
        self.add_cycles()