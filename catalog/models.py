from django.db import models

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите название"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="product",
        verbose_name="Изображение (превью)",
        **NULLABLE,
        help_text="Загрузите фото продукта",
    )
    category_name = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        help_text="Введите название категории",
        related_name='products'
    )
    price = models.IntegerField(verbose_name="Цена за покупку", help_text="Укажите цену")
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")
    manufactured_at = models.DateField(verbose_name="Дата производства", **NULLABLE)

    def __str__(self):
        return f"{self.name}, цена: {self.price}, категория: {self.category_name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category_name"]
