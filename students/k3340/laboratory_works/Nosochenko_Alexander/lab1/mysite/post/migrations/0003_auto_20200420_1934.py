# Generated by Django 3.0.5 on 2020-04-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200420_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.CharField(default='no category', max_length=400, verbose_name='Категория'),
        ),
    ]