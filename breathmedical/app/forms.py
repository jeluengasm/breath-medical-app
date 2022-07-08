from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Audio


class UserRegisterform(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    first_name = forms.CharField(
        required=True,
        max_length=254,
        widget=forms.TextInput(),
    )
    last_name = forms.CharField(
        required=True,
        max_length=254,
        widget=forms.TextInput(),
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class CreateAudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = (
            'instrument',
            'chest_location',
            'mode',
            'file',
            'comments',
        )

