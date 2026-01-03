from django.db import models

# Create your models here.
from django.urls import reverse
class Destination(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    best_time = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('hello:destination_detail', args=[self.slug])
