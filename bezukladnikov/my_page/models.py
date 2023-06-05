from django.db import models
from django.urls import reverse

class SportsGround(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('SportsGround', kwargs={'SportsGround_slug': self.slug})

    class Meta:
        verbose_name = 'Sports Ground'
        verbose_name_plural = 'Sports Ground'
        ordering = ['time_create', 'title'] # при выполнении команды objects.all() данные
        # будут отображаться уже отсортированными по полю создания, и потому уже по полю заголовок
        # если тут указать знак "-" перед названием полем, то сортировка будет в обратном порядке.

class City(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='City')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['id',]