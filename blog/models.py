from django.db import models

NULLABLE = {"null": True, "blank": True}


class Blog(models.Model):
    heading = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Придумайте заголовок статьи",
    )
    slag_blog = models.CharField(max_length=150, verbose_name="slag", **NULLABLE)
    text = models.TextField(
        help_text="Введите текст статьи", verbose_name="Текст статьи"
    )
    image = models.ImageField(upload_to="blog", verbose_name="Изображение", **NULLABLE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    view_counter = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return f"{self.heading}, Дата публикации: {self.create_date}, Количество просмотров: {self.view_counter}"

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"
        ordering = ["heading"]
