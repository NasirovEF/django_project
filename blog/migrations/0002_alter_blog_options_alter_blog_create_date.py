# Generated by Django 5.0.6 on 2024-05-31 22:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "ordering": ["heading"],
                "verbose_name": "Статья блога",
                "verbose_name_plural": "Статьи блога",
            },
        ),
        migrations.AlterField(
            model_name="blog",
            name="create_date",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                null=True,
                verbose_name="Дата",
            ),
        ),
    ]
