from email.mime import image
from pickle import TRUE
from tabnanny import verbose
from unicodedata import category
from django.apps.config import MODELS_MODULE_NAME
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='url')#фрагмент url адреса для категории

    class Meta: 
        db_table = 'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='url')#фрагмент url адреса для категории
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    image = models.ImageField(upload_to='goods_image', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name='Скидка в процентах')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество'),
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta: 
        db_table='product'
        verbose_name='продукт'
        verbose_name_plural = 'Продукты'