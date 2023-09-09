from django.db import models
from django_countries.fields import CountryField
from model_utils.models import TimeStampedModel

from apps.forum.models import Forum, Organization


# # Create your models here.
class Inivitation(TimeStampedModel, models.Model):
    code = models.IntegerField(unique=True)
    active = models.BooleanField(default=True)

    def __int__(self) -> int:
        return self.code


class User(TimeStampedModel, models.Model):
    forum_type = models.ManyToManyField(Forum)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    country = CountryField()
    passport = models.CharField(max_length=20)
    expire_date = models.DateField()
    image = models.ImageField(upload_to="media/profile/")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    access_id = models.CharField(max_length=30, blank=True, unique=True)
    invitation_id = models.ForeignKey(Inivitation, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name}-{self.last_name}"
