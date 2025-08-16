from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="yuzuki-no-mori")
    tagline = models.CharField(max_length=200, blank=True)
    about = models.TextField(blank=True)

    class Meta:
        verbose_name = "Site setting"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.site_name

