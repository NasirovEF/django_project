# Generated by Django 5.0.6 on 2024-05-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_product_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(verbose_name="Дата последнего изменения"),
        ),
    ]
