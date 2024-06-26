# Generated by Django 4.2.11 on 2024-05-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("task", models.CharField(max_length=500)),
                ("description", models.TextField()),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
