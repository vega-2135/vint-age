# Generated by Django 4.2.1 on 2024-05-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="product",
            name="rating",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
