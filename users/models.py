from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(
        'User photo',
        default='default_user_photo.png',
        upload_to='user_images'
    )

    def __str__(self):
        return f"Profile of {self.user.username}"
