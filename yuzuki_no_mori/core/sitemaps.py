# core/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from content.models import Article
from pages.models import Page

class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    def items(self): return Article.objects.published()
    def lastmod(self, obj): return obj.updated_at

class PageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    def items(self): return Page.objects.filter(is_published=True)
    def location(self, obj): return obj.get_absolute_url()

class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"
    def items(self): return ["home"]
    def location(self, item): return reverse(item)

