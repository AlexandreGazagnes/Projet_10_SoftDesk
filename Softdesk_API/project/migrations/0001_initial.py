# Generated by Django 5.0.3 on 2024-03-14 09:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=128, verbose_name="Titre")),
                ("description", models.TextField(blank=True, max_length=2048)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("frontend", "Frontend"),
                            ("backend", "Backend"),
                            ("ios", "iOS"),
                            ("android", "Android"),
                        ],
                        max_length=20,
                        verbose_name="Type",
                    ),
                ),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="authored_projects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "contributors",
                    models.ManyToManyField(
                        related_name="contributed_projects", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]