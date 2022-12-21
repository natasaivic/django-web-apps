# Generated by Django 4.1.4 on 2022-12-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("transaction_date", models.DateField()),
                ("post_date", models.DateField()),
                ("description", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=20)),
                ("transaction_type", models.CharField(max_length=20)),
                ("amount", models.CharField(max_length=20)),
            ],
        ),
    ]