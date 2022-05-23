from django.db import models
from accounts.models import User
# Create your models here.


class BaseStation(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name



