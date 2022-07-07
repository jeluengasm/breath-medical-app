from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path(
        'home/',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'login/',
        views.UserLoginView.as_view(),
        name='login'
    ),
    path(
        'register/',
        views.UserRegisterView.as_view(),
        name='register'
    ),
    path(
        'patient/<int:patient_id>/',
        views.PatientView.as_view(),
        name='patient'
    ),
    path(
        'patient/<int:id_patient>/analysis/<int:audio_id>/',
        views.AudioAnalysisView.as_view(),
        name='audio_analysis'
    ),
    path(
        'eda/',
        views.EDAView.as_view(),
        name='eda'
    ),
    path(
        'medic/<int:medic_id>/',
        views.MedicView.as_view(),
        name='medic'
    ),
    path(
        'medic/<int:pk>/history/<int:history_id>/',
        views.UserRegisterView.as_view(),
        name='history_medic'
    ),
    path(
        'medic/<int:medic_id>/history/<int:history_id>/new-audio/',
        views.NewAudioView.as_view(),
        name='new_audio'
    ),
]