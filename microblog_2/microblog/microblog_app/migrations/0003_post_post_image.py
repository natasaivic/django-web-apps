# Generated by Django 4.1.1 on 2023-01-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("microblog_app", "0002_remove_post_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_image",
            field=models.ImageField(default=0, upload_to="images/"),
        ),
    ]
