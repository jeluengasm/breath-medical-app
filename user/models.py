from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager

from django.core.validators import RegexValidator


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='email address', unique=True)

    age = models.FloatField(null=True, verbose_name='age')

    sex = models.CharField(
        choices=(
            ('M', 'Male'),
            ('F', 'Female'),
            ('I', 'Intersexual'),
            ('N', 'No response'),
        ),
        verbose_name='sex',
        max_length=11,
        blank=True,
    )

    city = models.ForeignKey(
        'app.City',
        verbose_name='city',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        blank=True,
        max_length=15,
        verbose_name='phone number',
        validators=[
            RegexValidator(r'^[0-9]*$', message='only numbers'),
        ],
    )

    legal_id_type = models.CharField(
        max_length=10,
        choices=(
            ('TI', 'TI'),
            ('CC', 'CC'),
            ('NIT', 'NIT'),
            ('Pass', 'Passport'),
        ),
        verbose_name='ID type',
        default='CC',
    )

    legal_id = models.CharField(
        max_length=10,
        verbose_name='legal ID',
    )

    address = models.CharField(
        max_length=128,
        verbose_name='address',
        blank=True,
    )

    photo = models.ImageField(
        upload_to='',
        max_length=100,
        verbose_name='photo',
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now,
    )

    blood_type = models.CharField(
        choices=(
            ('A', 'A'),
            ('B', 'B'),
            ('AB', 'AB'),
            ('O', 'O'),
        ),
        max_length=2,
        verbose_name='blood type',
        default='A',
    )

    rh_factor = models.CharField(
        choices=(
            ('+', '+'),
            ('-', '-'),
        ),
        max_length=1,
        verbose_name='rh factor',
        default='+'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name

    def __repr__(self):
        return self.get_full_name


class Doctor(User):
    medical_areas = models.ManyToManyField('app.MedicalArea',verbose_name='medical areas')

    role = models.CharField(
        max_length=30,
        verbose_name='role',
        default='',
    )

    def __str__(self):
        return f'Dr. {self.get_full_name}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'


class Patient(User):
    adult_bmi = models.PositiveSmallIntegerField(null=True, verbose_name='adult BMI')

    child_height = models.PositiveSmallIntegerField(null=True, verbose_name='child weight')

    child_weight = models.PositiveSmallIntegerField(null=True, verbose_name='child weight')

    def __str__(self):
        return self.get_full_name

    # def __repr__(self):
    #     return self.get_full_name

    class Meta:
        ordering = ['-id']
        verbose_name = 'patient'
        verbose_name_plural = 'patients'