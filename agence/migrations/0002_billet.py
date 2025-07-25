# Generated by Django 5.2.2 on 2025-07-19 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=100)),
                ('date_depart', models.DateField()),
                ('heure_depart', models.TimeField()),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agence.agence')),
            ],
        ),
    ]
