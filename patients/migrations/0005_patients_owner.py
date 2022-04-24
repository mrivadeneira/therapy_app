# Generated by Django 4.0.2 on 2022-03-09 23:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0004_alter_shifts_day_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=models.SET('DELETED'), related_name='owner_patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
