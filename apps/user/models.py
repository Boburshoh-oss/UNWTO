from django.db import models
from django_countries.fields import CountryField
from model_utils.models import TimeStampedModel
from apps.forum.models import Forum, Organization

# Create your models here.
class Inivitation(TimeStampedModel, models.Model):
    code = models.CharField(unique=True, max_length=255)
    amount = models.IntegerField(default=10, blank=True,null=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.code


class User(TimeStampedModel, models.Model):
    forum_type = models.ManyToManyField(Forum)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    country = CountryField()
    org_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    passport = models.CharField(max_length=20)
    expire_date = models.DateField()
    image = models.ImageField(upload_to="media/profile/")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    access_id = models.CharField(max_length=30, blank=True, unique=True, null=True)
    invitation_id = models.ForeignKey(Inivitation, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13,blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.first_name}-{self.last_name}"
