# Generated by Django 5.2.2 on 2025-06-19 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_depart', models.DateTimeField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nombre_places', models.PositiveIntegerField()),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.trajet')),
            ],
        ),
        migrations.AddField(
            model_name='trajet',
            name='arrivee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivee', to='reservation.ville'),
        ),
        migrations.AddField(
            model_name='trajet',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='reservation.ville'),
        ),
    ]
