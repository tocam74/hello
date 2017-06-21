from django.db import models
from django.contrib.auth.models import User

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Loonatic(Timestamp):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/loonatics/%s/" % self.slug

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

def get_image_path(instance, filename):
    return '/'.join(['loonatic_images', instance.loonatic.slug, filename])

class Upload(Timestamp):
    loonatic = models.ForeignKey(Loonatic, related_name="uploads")
    image = models.ImageField(upload_to=get_image_path)
