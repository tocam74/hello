from django.db import models
from django.contrib.auth.models import User

class Loonatic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, null=True, blank=True)

class Social(models.Model):
    SOCIAL_TYPES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('pinterest', 'Pinterest'),
    )

    network = models.CharField(max_length=255, choices=SOCIAL_TYPES)
    username = models.CharField(max_length=255)
    loonatic = models.ForeignKey(Loonatic, related_name="social_accounts")

    class Meta:
        verbose_name_plural = "Social media links"
