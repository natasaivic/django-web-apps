# Generated by Django 4.1.4 on 2022-12-28 19:30

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
                ("title", models.CharField(max_length=200)),
                ("text", models.CharField(max_length=3000)),
                ("image", models.ImageField(upload_to="")),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
