# Generated by Django 4.2.8 on 2023-12-09 13:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_rename_height_prediction_avg_blood_glucose_level_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="prediction",
            old_name="AVG_BLOOD_GLUCOSE_LEVEL",
            new_name="avg_glucose_level",
        ),
    ]
