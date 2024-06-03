# Generated by Django 4.2.1 on 2024-05-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ReachOut",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "order_number",
                    models.CharField(blank=True, max_length=32, null=True),
                ),
                (
                    "about",
                    models.CharField(
                        choices=[
                            ("general", "General Question"),
                            ("order", "About an order"),
                            ("other", "Something else"),
                        ],
                        max_length=10,
                    ),
                ),
                ("message", models.TextField()),
                ("read", models.BooleanField(default=False)),
            ],
        ),
    ]
