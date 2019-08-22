from django.db import models
from django.urls import reverse


class Video(models.Model):
    slug = models.CharField(max_length=32)
    titulo = models.CharField(max_length=32)
    vimeo_id = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))