# Generated by Django 5.0.6 on 2024-06-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="Дата создания"),
        ),
    ]
