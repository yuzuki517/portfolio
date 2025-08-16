# pages/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *a, **kw):
        if not self.slug: self.slug = slugify(self.title)
        return super().save(*a, **kw)

    def get_absolute_url(self): return reverse("pages:detail", args=[self.slug])
    def __str__(self): return self.title

