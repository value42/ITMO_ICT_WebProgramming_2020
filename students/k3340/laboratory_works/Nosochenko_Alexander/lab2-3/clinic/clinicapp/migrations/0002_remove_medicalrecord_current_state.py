# Generated by Django 3.0.7 on 2020-07-01 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='current_state',
        ),
    ]