from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager

from django.core.validators import RegexValidator


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='email address', unique=True)

    phone_number = models.CharField(
        blank=True,
        max_length=15,
        verbose_name='phone number',
        validators=[
            RegexValidator(r'^[0-9]*$', message='only numbers'),
        ],
    )

    birthday = models.DateTimeField(
        verbose_name='birthday',
        default=timezone.now,
    )

    legal_id_type = models.CharField(
        max_length=3,
        choices=(('CC', 'CC'), ('NIT', 'NIT')),
        verbose_name='ID type',
        default='CC',
    )

    legal_id = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='legal id',
        default='',
    )

    address = models.CharField(
        max_length=128,
        verbose_name='address',
        default='',
    )

    photo = models.ImageField(
        upload_to='uploads/',
        max_length=100,
        verbose_name='photo',
        blank=True
    )

    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now,
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.email


class Doctor(User):
    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['-id']
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'


class Patient(User):
    attending_doctor = models.ForeignKey(Doctor, verbose_name='doctor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['-id']
        verbose_name = 'patient'
        verbose_name_plural = 'patients'