from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from django.core.exceptions import PermissionDenied
from breathmedical import settings
from app import forms
from app.models import *
from user.models import *

from keras.models import model_from_json
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import librosa


class Diagnosis():
    def __init__(self, id, diagnosis, image_path):
        self.id = id
        self.diagnosis = diagnosis
        self.image_path = image_path

def get_wav_files():
    audio_path = 'app/processing/data/Respiratory_Sound_Database/audio_and_txt_files/'
    files = [f for f in listdir(audio_path) if isfile(
        join(audio_path, f))]  # Gets all files in dir
    wav_files = [f for f in files if f.endswith('.wav')]  # Gets wav files
    wav_files = sorted(wav_files)
    return wav_files, audio_path


def diagnosis_data():
    diagnosis = pd.read_csv('app/processing/data/Respiratory_Sound_Database/patient_diagnosis.csv')

    wav_files, audio_path = get_wav_files()
    diag_dict = {101: "URTI"}
    diagnosis_list = []

    for index, row in diagnosis.iterrows():
        diag_dict[row[0]] = row[1]

    c = 0
    for f in wav_files:
        diagnosis_list.append(
            Diagnosis(c, diag_dict[int(f[:3])], audio_path+f))
        c += 1

    return diagnosis_list


def audio_features(filename):
    sound, sample_rate = librosa.load(filename)

    stft = np.abs(librosa.stft(sound))
    # Mel-frequency cepstral coefficients (MFCCs)
    mfccs = np.mean(librosa.feature.mfcc(
        y=sound, sr=sample_rate, n_mfcc=40), axis=1)
    # Compute a chromagram from a waveform or power spectrogram.
    chroma = np.mean(librosa.feature.chroma_stft(
        S=stft, sr=sample_rate), axis=1)
    # Compute a mel-scaled spectrogram.
    mel = np.mean(librosa.feature.melspectrogram(
        y=sound, sr=sample_rate), axis=1)
    # Compute spectral contrast
    contrast = np.mean(librosa.feature.spectral_contrast(
        S=stft, sr=sample_rate), axis=1)
    # Computes the tonal centroid features (tonnetz)
    tonnetz = np.mean(librosa.feature.tonnetz(
        y=librosa.effects.harmonic(sound), sr=sample_rate), axis=1)

    concat = np.concatenate((mfccs, chroma, mel, contrast, tonnetz))
    return concat


#TODO reubicar
class UserLoginView(TemplateView):
    template_name = 'app/login_form.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserRegisterView(FormView):
    template_name = 'app/register_form.html'
    form_class = forms.UserRegisterform
    success_url = reverse_lazy('app:login')

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        form.save()
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'app/home.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context


class PatientView(TemplateView):
    template_name = 'app/patient.html'
    patient_id = None

    def dispatch(self, request, *args, **kwargs):
        self.patient_id = kwargs.pop('patient_id', None)
        if self.patient_id != 1:
            raise PermissionDenied("Not allowed. This user id doesn't exist")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient_id"] = self.patient_id
        context["BASE_DIR"] = settings.BASE_DIR
        return context


class MedicView(TemplateView):
    template_name = 'app/medic.html'
    medic_id = None

    def dispatch(self, request, *args, **kwargs):
        self.medic_id = kwargs.pop('medic_id', None)
        if self.medic_id != 1:
            raise PermissionDenied("Not allowed. This user id doesn't exist")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medic_id"] = self.medic_id
        context["BASE_DIR"] = settings.BASE_DIR
        return context


class NewAudioView(CreateView):
    template_name = 'app/new_audio.html'
    medic = None
    user_history = None
    audio = None
    form_class = forms.CreateAudioForm


    def get_success_url(self):
        return reverse('app:audio_analysis', kwargs={
                'history_id': self.user_history.id, 'audio_id': self.audio.id
                })

    def dispatch(self, request, *args, **kwargs):
        self.medic = Doctor.objects.get(id=kwargs.pop('medic_id', None))
        self.user_history = UserHistory.objects.get(id=kwargs.pop('history_id', None))
        if not self.medic or not self.user_history:
            raise PermissionDenied("Not allowed.")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medic"] = self.medic
        context["BASE_DIR"] = settings.BASE_DIR
        return context

    def predict_patient_audio(self, file_path):
        # load json and create model
        json_file = open('app/processing/data/model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("app/processing/data/model.h5")
        print("Loaded model from disk")
        print(loaded_model.summary())

        Audioprueba = audio_features(file_path)
        y = np.expand_dims(Audioprueba, 0)
        z = np.expand_dims(y, -1)
        test = loaded_model.predict(z)
        one_hot = {0: "COPD", 1: "Healthy", 2: "URTI", 3: "Bronchiectasis",
                4: "Pneumonia", 5: "Bronchiolitis", 6: "Asthma", 7: "LRTI"}
        clase = int(np.argmax(test, axis=1))

        return (one_hot[clase])

    def form_valid(self, form):
        self.audio = form.save()
        self.audio.audio_filename = f'{self.audio.id}_{self.audio.chest_location}' \
                                    f'_{self.audio.mode}_{self.audio.instrument.name}'
        self.audio.city = self.medic.city
        self.audio.user_history = self.user_history
        self.audio.diagnosis = self.predict_patient_audio(self.audio.file.url[1:])
        self.audio.save()

        return super().form_valid(form)



class AudioAnalysisView(TemplateView): #DetailView
    template_name = 'app/audio_analysis.html'
    patient = None
    user_history = None
    audio = None

    def dispatch(self, request, *args, **kwargs):
        self.audio = Audio.objects.get(id=kwargs.pop('audio_id', None))
        self.user_history = UserHistory.objects.get(id=kwargs.pop('history_id', None))
        self.patient = self.user_history.patient
        self.doctor = self.user_history.doctor
        
        if not self.patient or not self.doctor or not self.user_history:
            raise PermissionDenied('Not allowed.')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = self.patient
        context['doctor'] = self.doctor
        context['audio'] = self.audio
        context['history'] = self.user_history
        context['BASE_DIR'] = settings.BASE_DIR
        return context

class EDAView(TemplateView): 
    template_name = 'app/eda.html'
