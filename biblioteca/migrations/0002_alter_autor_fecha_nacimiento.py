# Generated by Django 5.2.3 on 2025-07-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
