# Generated by Django 4.2.2 on 2023-06-14 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calories",
            name="calories",
            field=models.PositiveIntegerField(),
        ),
    ]
