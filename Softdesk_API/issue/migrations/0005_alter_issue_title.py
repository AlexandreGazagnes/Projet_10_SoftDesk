# Generated by Django 5.0.3 on 2024-03-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issue", "0004_alter_issue_contributor_assigned"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="title",
            field=models.CharField(max_length=128, unique=True),
        ),
    ]