from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    bio = models.TextField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    reputation = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    facebook_handle = models.CharField(max_length=100, blank=True, null=True)
    linkedIn_handle = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)

    # TODO create a custom field to fill reputation

    def __str__(self):
        return self.username
