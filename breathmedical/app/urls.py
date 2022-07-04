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
        'patient/<int:patient_id>',
        views.PatientView.as_view(),
        name='patient'
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
]