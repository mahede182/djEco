from django.db import models

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    site_name = models.CharField(max_length=100, default='VIOLET')

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_name