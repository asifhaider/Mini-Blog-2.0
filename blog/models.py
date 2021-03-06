from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #unrestricted length
    date_posted = models.DateTimeField(default=timezone.now) # while creating new instance update date time
    author = models.ForeignKey(User, on_delete=models.CASCADE) #user deleted, auto deletes posts

    # dunder means double underscore, magic methods or bla bla
    # declared to return title in shell sql manipulation

    def __str__(self):
        return self.title

    # reverse will return the full route, as a string unlike redirect

    def get_absolute_url (self):
        return reverse ('post-detail', kwargs = {'pk': self.pk})
