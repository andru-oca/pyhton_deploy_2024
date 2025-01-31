# Generated by Django 5.0.6 on 2024-07-01 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pelicula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200, unique=True)),
                ("duracion", models.IntegerField()),
                ("genero", models.CharField(max_length=200)),
                ("fecha_release", models.DateField(default=datetime.date.today)),
            ],
            options={
                "db_table": "peliculas_mysql",
            },
        ),
    ]
