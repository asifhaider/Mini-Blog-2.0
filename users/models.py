from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # delete profile auto if user deleted, nut not vice versa
    image = models.ImageField (default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"