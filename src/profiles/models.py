from django.contrib.auth.models import AbstractUser
from django.db import models


class UserNet(AbstractUser):
    """Custom user model"""
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other')
    )
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    user_url = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='other')
