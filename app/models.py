from sunau import AUDIO_FILE_ENCODING_ADPCM_G721
from tabnanny import verbose
from django.db import models
from django.utils import timezone

from django.core.validators import RegexValidator


class Hospital(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='name',
    )

    address = models.CharField(
        max_length=255,
        verbose_name='address',
    )

    phone_number = models.CharField(
        blank=True,
        max_length=15,
        verbose_name='phone number',
        validators=[
            RegexValidator(r'^[0-9]*$', message='only numbers'),
        ],
    )

    legal_id = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='legal id',
        default='',
    )

    city = models.ForeignKey(
        'app.City',
        verbose_name='city',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    medical_areas = models.ManyToManyField('app.MedicalArea',verbose_name='medical areas')

    patients = models.ManyToManyField('user.Patient', verbose_name='patients')

    doctors = models.ManyToManyField('user.Doctor', verbose_name='doctors')

    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now,
    )

    class Meta:
        verbose_name = 'hospital'
        verbose_name_plural = 'hospitals'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hospital_detail',
        kwargs={'pk': self.pk})


class City(models.Model):
    name = models.CharField(
        max_length=100,
        null=True
    )

    country = models.ForeignKey(
        'app.Country',
        verbose_name='country',
        on_delete=models.SET_NULL,
        null=True,
    )

    population = models.PositiveIntegerField(verbose_name='population', null=True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city_detail',
        kwargs={'pk': self.pk})


class MedicalArea(models.Model):
    title = models.CharField(max_length=100)

    description = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name = 'medical area'
        verbose_name_plural = 'medical areas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('MedicalArea_detail',
        kwargs={'pk': self.pk})


class Country(models.Model):
    name = models.CharField(verbose_name='name', max_length=50)

    population = models.PositiveBigIntegerField(verbose_name='population', null=True)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country_detail',
        kwargs={'pk': self.pk})


class Audio(models.Model):
    audio_filename = models.CharField(
        verbose_name='audio filename',
        blank=True,
        max_length=50,
    )
    
    instrument = models.ForeignKey(
        'app.MedicalInstrument',
        verbose_name='instrument',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    city = models.ForeignKey(
        'app.City',
        verbose_name='city',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    chest_location = models.CharField(
        choices=(
            ('Tc', 'Trachea'),
            ('Al', 'Anterior left'),
            ('Ar', 'Anterior right'),
            ('Pl', 'Posterior left'),
            ('Pr', 'Posterior right'),
            ('Ll', 'Lateral left'),
            ('Lr', 'Lateral right'),
        ),
        verbose_name='body location',
        max_length=15,
    )

    mode = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='mode',
        choices=(
            ('sc', 'Sequential/Single channel (sc)'),
            ('mc', 'Simultaneus/Multi-channel (mc)'),
        )
    )

    comments = models.TextField(max_length=255, blank=True, verbose_name='comments')

    user_history = models.ForeignKey(
        'app.UserHistory',
        verbose_name='user history',
        on_delete=models.SET_NULL,
        null=True,
    )

    file = models.FileField(
        upload_to='audio/%Y/%m/%d/',
        max_length=2000, #TODO
        verbose_name='audio file',
        blank=True,
    )

    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now,
    )

    diagnosis = models.CharField(
        max_length=100,
        verbose_name='diagnosis',
        blank=True,
    )

    class Meta:
        verbose_name = 'audio'
        verbose_name_plural = 'audios'

    def __str__(self):
        return self.audio_filename

    def get_absolute_url(self):
        return reverse('audio_detail',
        kwargs={'pk': self.pk})


class Cycle(models.Model):
    audio = models.ForeignKey('app.Audio', verbose_name='audio file', on_delete=models.CASCADE)

    numestdo = models.CharField(
        verbose_name='health status',
        choices=(
            ('0', 'Health'),
            ('1', 'Wheezing'),
            ('2', 'Crackle'),
            ('3', 'Twice')
        ),
        max_length=10,
    ) #TODO

    begin_cycle = models.FloatField(
        verbose_name='begin cycle', null=True
    )

    end_cycle = models.FloatField(
        verbose_name='end cycle', null=True
    )
    
    status = models.CharField(
        choices=(
            ('Normal', 'Normal'),
            ('Wheeze', 'Wheeze'),
            ('Crackle', 'Crackle'),
            ('Twice', 'Wheeze and Crackle'),
        ),
        max_length=18,
        verbose_name='status',
    )

    variance = models.FloatField(verbose_name='variance', null=True)

    range_cycle =  models.FloatField(verbose_name='range', null=True)

    sma_coarse = models.FloatField(verbose_name='SMA coarse', null=True)

    sma_fine = models.FloatField(verbose_name='SMA fine', null=True)

    avg_spectre = models.FloatField(verbose_name='average spectre', null=True)

    diagnosis = models.CharField(
        max_length=100,
        verbose_name='diagnosis',
        blank=True,
    )

    class Meta:
        verbose_name = 'cycle'
        verbose_name_plural = 'cycles'

    def __str__(self):
        return f'Cycle #{self.pk}'

    def __repr__(self):
        return f'Cycle #{self.pk}'

    def get_absolute_url(self):
        return reverse('cycle_detail',
        kwargs={'pk': self.pk})


class UserHistory(models.Model):
    patient = models.ForeignKey('user.Patient', verbose_name='patient', on_delete=models.SET_NULL, null=True)

    doctor = models.ForeignKey('user.Doctor', verbose_name='doctor', on_delete=models.SET_NULL, null=True)

    suggestions = models.TextField(max_length=255, blank=True, verbose_name='suggestions')

    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now,
    )

    class Meta:
        verbose_name = 'user\'s history'
        verbose_name_plural = 'user\'s histories'

    def __str__(self):
        return f'User history #{self.id}'

    def __repr__(self):
        return f'User history #{self.id}'

    def get_absolute_url(self):
        return reverse('user_history_detail',
        kwargs={'pk': self.pk})


class MedicalInstrument(models.Model):
    name = models.CharField(max_length=50)

    brand = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name ='medical instrument'
        verbose_name_plural ='medical instruments'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('MedicalInstrument_detail', kwargs={'pk': self.pk})
