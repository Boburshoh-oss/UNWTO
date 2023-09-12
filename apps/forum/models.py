from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.


class Organization(TimeStampedModel, models.Model):
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Forum(TimeStampedModel, models.Model):
    CHOICES =(
    ("GA", "General Assambly"),
    ("IF", "Investment Forum"),
    ("EF", "Educational Forum"),
)   
    title = models.CharField(max_length=255, blank=True)
    short_key=models.CharField(choices=CHOICES, default="GA",max_length=255,) 
    organization = models.ManyToManyField(Organization)
    description = models.TextField()

    def __str__(self):
        return self.title


class ForumProject(TimeStampedModel, models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="media/projects/")
    context = models.TextField()

    def __str__(self):
        return self.title


class Event(TimeStampedModel, models.Model):
    day = models.CharField(max_length=255)
    date = models.DateField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    ordered = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f"{self.day} {self.forum.title}"

class EventTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description[:20]
