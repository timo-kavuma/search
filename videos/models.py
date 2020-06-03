from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    url = models.URLField(max_length=255)
    embed = models.URLField(max_length=255)
    title = models.TextField()
    slug = models.SlugField(default='', editable=False, max_length=255)
    description = models.TextField(default='', blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    dateadded = models.CharField(max_length=50, blank=True, null=True)
    screenshot = models.URLField(max_length=255, default='')
    trailer = models.URLField(max_length=255, default='', blank=True, null=True)
    actors = models.TextField(default='', blank=True, null=True)
    tags = ArrayField(models.TextField(default='', blank=True, null=True))
    flipbook = ArrayField(models.TextField(default=''), blank=True, null=True)
    mediatype = models.CharField(max_length=50)
    partner = models.CharField(max_length=50)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'videos'

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('video_detail', args=[str(self.slug)])
