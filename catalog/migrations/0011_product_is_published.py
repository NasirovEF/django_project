# Generated by Django 4.2 on 2024-06-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_alter_version_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Статус публикации"),
        ),
    ]
