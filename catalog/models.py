from django.db import models, connection

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE"
            )

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
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Укажите цену"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE"
            )

    def __str__(self):
        return f"{self.name}, цена: {self.price}, категория: {self.category_name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category_name"]

