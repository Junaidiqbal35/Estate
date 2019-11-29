from django.db import models
from _datetime import datetime
from django.contrib.auth.models import User

class Profile(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(max_length=20)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  bio = models.TextField(blank=True)

  def __str__(self):
      return self.user.username