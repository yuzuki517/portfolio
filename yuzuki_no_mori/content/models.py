# content/models.py
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="PUBLISHED")

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    def save(self, *a, **kw):
        if not self.slug: self.slug = slugify(self.name)
        return super().save(*a, **kw)
    def __str__(self): return self.name

class Article(models.Model):
    STATUS = (("DRAFT", "Draft"), ("PUBLISHED", "Published"))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    body = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default="DRAFT")
    preview_token = models.CharField(max_length=36, blank=True, editable=False)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    published = PublishedManager()

    def save(self, *a, **kw):
        if not self.slug: self.slug = slugify(self.title)
        if not self.preview_token: self.preview_token = uuid.uuid4().hex
        return super().save(*a, **kw)

    def get_absolute_url(self):
        return reverse("content:detail", args=[self.slug])

    def __str__(self): return self.title

