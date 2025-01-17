from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class doctor(models.Model):
    profile_photo = models.ImageField(upload_to='images/Doctor_profile_photo', blank=True, null=True, default="doctorProfilePhoto/avatar.svg")
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    specialities = TaggableManager()
    ratings = models.IntegerField(blank=True, null=True)
    auth_token = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name
    