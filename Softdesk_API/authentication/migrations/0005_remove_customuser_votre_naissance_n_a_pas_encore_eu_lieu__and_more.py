# Generated by Django 5.0.3 on 2024-03-14 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        (
            "authentication",
            "0004_remove_customuser_date_of_birth_must_be_in_past_and_more",
        ),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="customuser",
            name="Votre naissance n'a pas encore eu lieu !!!",
        ),
        migrations.RemoveConstraint(
            model_name="customuser",
            name="Vous devez avoir plus de 15 ans !!!",
        ),
        migrations.AddConstraint(
            model_name="customuser",
            constraint=models.CheckConstraint(
                check=models.Q(("date_of_birth__lt", datetime.date(2024, 3, 14))),
                name="Votre naissance n'a pas encore eu lieu !!!",
            ),
        ),
        migrations.AddConstraint(
            model_name="customuser",
            constraint=models.CheckConstraint(
                check=models.Q(("date_of_birth__lt", datetime.date(2009, 3, 18))),
                name="Vous devez avoir plus de 15 ans !!!",
            ),
        ),
    ]
