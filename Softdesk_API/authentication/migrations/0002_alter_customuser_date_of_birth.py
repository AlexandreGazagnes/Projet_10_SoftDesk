# Generated by Django 5.0.3 on 2024-03-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="date_of_birth",
            field=models.DateField(),
        ),
    ]