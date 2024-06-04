from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='cars/photo', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку', blank=True,
                                null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    view_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите колличество просмотров',
        default=0
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='cars/image', blank=True, null=True, verbose_name='Изображение')
    public = models.IntegerField(verbose_name='признак публикации', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.CharField(max_length=100, verbose_name='slug', blank=True, null=True)

    view_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите колличество просмотров',
        default=0
    )

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'{self.title} {self.description} {self.public} {self.created_at}'