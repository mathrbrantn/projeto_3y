# coding=utf-8

from django.db import models
from datetime import date


class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Slug')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class ProductManager(models.Manager):

    def approved(self):
        return self.filter(is_approved=True)


class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    instrutor = models.CharField('Instrutor', max_length=100)
    image = models.ImageField('Imagem', upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    slug = models.SlugField('Slug')
    category = models.ForeignKey(Category, verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    is_approved = models.BooleanField('Aprovado', default=True, blank=True)
    price = models.DecimalField(
        'Preço', default=0, decimal_places=2, max_digits=8
    )
    date = models.DateField(("Data"), default=date.today)
    objects = ProductManager()

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name
