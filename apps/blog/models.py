from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Banner(TimeStampedModel, models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/banner/")

    def __str__(self) -> str:
        return self.title


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    logo = models.FileField(upload_to="media/logo/")

class Contact(models.Model):
    TYPES = (
        (0, "Link"),
        (1, "Email"),
        (2, "Telefon"),
    )
    title = models.CharField(max_length=255, blank=True)
    type =models.IntegerField(choices=TYPES, default=2)
    name = models.CharField(max_length=20, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title
