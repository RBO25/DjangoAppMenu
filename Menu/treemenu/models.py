from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название меню')
    slug = models.SlugField(max_length=255, verbose_name='slug')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, verbose_name="slug")
    menu = models.ForeignKey(Menu, blank=True, related_name='categorys', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'

    def __str__(self):
        return self.name