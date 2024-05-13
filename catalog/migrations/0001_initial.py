# Generated by Django 5.0.6 on 2024-05-13 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                ("description", models.TextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите название",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта", verbose_name="Описание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото продукта",
                        null=True,
                        upload_to="product",
                        verbose_name="Изображение (превью)",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Укажите цену", verbose_name="Цена за покупку"
                    ),
                ),
                ("created_at", models.DateField(verbose_name="Дата создания")),
                (
                    "updated_at",
                    models.DateField(verbose_name="Дата последнего изменения"),
                ),
                (
                    "category_name",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите название категории",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "category_name"],
            },
        ),
    ]