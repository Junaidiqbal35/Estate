from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    host_name = models.CharField(max_length=200, default='juni')
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    reply = models.ForeignKey('Contact',on_delete=models.CASCADE,null=True, related_name='replies')
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    host_id = models.IntegerField(default=0)
    host_email = models.CharField(max_length=200, default='juni@gmail.com')
    user_photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank='default.jpg')
    host_photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank= 'glasses.jpg')
    listing_photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank='asd.jpg')

    def __str__(self):
        return self.name



class Inbox(models.Model):
     listing = models.CharField(max_length=200, default='Junaid')
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
     reciever =  models.ForeignKey(User,on_delete=models.CASCADE, related_name="rciever")
     message = models.TextField(blank=False)
     created_at = models.DateTimeField(default=datetime.now, blank=True)

     def __str__(self):
        return self.message