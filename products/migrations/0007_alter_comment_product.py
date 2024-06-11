# Generated by Django 4.2.1 on 2024-06-07 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="products.product",
            ),
        ),
    ]
