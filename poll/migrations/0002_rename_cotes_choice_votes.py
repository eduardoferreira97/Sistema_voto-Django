# Generated by Django 4.1 on 2022-12-05 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("poll", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice", old_name="cotes", new_name="votes",
        ),
    ]
