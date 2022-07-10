from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Doctor, Patient


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)


class DoctorCreationForm(UserCreationForm):

    class Meta:
        model = Doctor
        fields = ('email',)


class DoctorChangeForm(UserChangeForm):

    class Meta:
        model = Doctor
        fields = ('email',)

class PatientCreationForm(UserCreationForm):

    class Meta:
        model =Patient
        fields = ('email',)


class PatientChangeForm(UserChangeForm):

    class Meta:
        model =Patient
        fields = ('email',)