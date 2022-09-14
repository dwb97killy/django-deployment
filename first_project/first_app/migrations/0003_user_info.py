# Generated by Django 4.1 on 2022-09-14 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0002_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="User_info",
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
                ("portfolio_site", models.URLField(blank=True)),
                (
                    "profile_pic",
                    models.ImageField(blank=True, upload_to="profile_pics"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="first_app.user"
                    ),
                ),
            ],
        ),
    ]