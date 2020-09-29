from django.db import models
from datetime import date


class Category(models.Model):
    category = models.CharField('Категория', max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    publication_date = models.DateField('Дата публикации', default=date.today)
    content = models.TextField('Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
