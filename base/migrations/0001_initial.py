# Generated by Django 4.2.8 on 2023-12-06 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Prediction",
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
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=10
                    ),
                ),
                ("age", models.IntegerField()),
                ("height", models.FloatField()),
                ("weight", models.FloatField()),
                (
                    "smoking_status",
                    models.CharField(
                        choices=[
                            ("never", "Never Smoked"),
                            ("formerly", "Formerly Smoked"),
                            ("smokes", "Currently Smokes"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "risk",
                    models.IntegerField(choices=[(0, "Low Risk"), (1, "High Risk")]),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="predictions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
    ]