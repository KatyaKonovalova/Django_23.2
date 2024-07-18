from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите название категории",
        related_name="products",
    )
    price = models.FloatField(verbose_name="Цена", help_text="Введите цену товара")
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Вставьте фотографию товара",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        blank=True,
        auto_now_add=True,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
        blank=True,
        auto_now=True,
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        blank=True,
        null=True,
        related_name="products",
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "description"]
        permissions = [
            ("can_edit_category", "Can edit category"),
            ("can_edit_description", "Can edit derscription"),
            ("can_cancel_publication", "Can cancel publication"),
        ]

    def __str__(self):
        return f"{self.name} - {self.price}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
        help_text="Выберите продукт",
    )
    version_number = models.CharField(
        max_length=10,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
        null=True,
        blank=True,
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
        null=True,
        blank=True,
    )
    is_version_active = models.BooleanField(
        default=False,
        verbose_name="Активная версия",
        help_text="Является ли версия активной",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name
