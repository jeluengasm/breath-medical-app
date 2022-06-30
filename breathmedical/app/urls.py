from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)