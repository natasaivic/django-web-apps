# Generated by Django 4.1.4 on 2022-12-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("text", models.CharField(max_length=1000)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subscribe",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
