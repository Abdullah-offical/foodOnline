# Generated by Django 5.1.2 on 2024-10-22 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="first_last",
            new_name="last_name",
        ),
    ]
