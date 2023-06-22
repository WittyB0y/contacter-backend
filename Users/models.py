from django.contrib.auth.models import User
from django.db import models


class Photo_Main_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_path = models.ImageField(upload_to='photos/main/')
    loaded_photo = models.DateTimeField(auto_now_add=True)
    updated_photo = models.DateTimeField(auto_now=True)
