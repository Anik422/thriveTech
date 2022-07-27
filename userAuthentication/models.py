from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    facebook_id = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to="userProfileImage", blank=True)

    def __str__(self):
        return self.user.username