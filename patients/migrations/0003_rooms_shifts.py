# Generated by Django 4.0.1 on 2022-02-23 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0002_alter_therapists_id_document_n'),
        ('patients', '0002_alter_patients_id_document_n'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_recurrent', models.BooleanField(default=False)),
                ('day_start', models.DateField()),
                ('day_end', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_shift', to='patients.rooms')),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_shift', to='therapists.therapists')),
            ],
            options={
                'unique_together': {('room', 'day_start', 'time_start')},
            },
        ),
    ]