from django.db import models
from django.urls import reverse

class SportsGround(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Sports Ground'
        verbose_name_plural = 'Sports Ground'
        ordering = ['time_create', 'title']

class City(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='City')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['id',]