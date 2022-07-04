# Generated by Django 4.0.5 on 2022-07-04 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='location',
            new_name='chest_location',
        ),
        migrations.RemoveField(
            model_name='cycle',
            name='interval',
        ),
        migrations.AddField(
            model_name='audio',
            name='audio_filename',
            field=models.CharField(blank=True, max_length=50, verbose_name='audio filename'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='begin_cycle',
            field=models.FloatField(null=True, verbose_name='begin cycle'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=100, verbose_name='diagnosis'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='end_cycle',
            field=models.FloatField(null=True, verbose_name='end cycle'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.city', verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(blank=True, max_length=2000, upload_to='audio/%Y/%m/%d/', verbose_name='audio file'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='instrument',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.medicalinstrument', verbose_name='instrument'),
        ),
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.PositiveIntegerField(null=True, verbose_name='population'),
        ),
        migrations.AlterField(
            model_name='medicalarea',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
