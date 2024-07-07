# Generated by Django 4.2 on 2024-06-30 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0013_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category_name"],
                "permissions": [
                    ("сan_published", "Может изменять статус публикации продукта"),
                    ("сan_edit_description", "Может изменять описание продукта"),
                    ("сan_edit_category", "Может изменять категорию продукта"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]