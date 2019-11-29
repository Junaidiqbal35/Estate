
from django.db import models
from _datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

from host.models import Host


class Listing(models.Model):

  host = models.ForeignKey (User, on_delete=models.CASCADE,default=1 )
  #host = models.ForeignKey(User,on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zipcode = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  rules = models.TextField(blank=True)
  price = models.IntegerField()
  attendies = models.IntegerField(default=5)
  bedrooms = models.IntegerField(blank=True)
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  wifi=  models.BooleanField(default=True)
  favourite = models.ManyToManyField(User, related_name= 'favourite', blank=True)
  garage= models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5,decimal_places=1)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now,blank=True)



  def __str__(self):
      return  self.title
  def get_absolute_url(self):
    return reverse("listings", kwargs={"id": self.id})

class Comment(models.Model):
  listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=1)
  user = models.ForeignKey (User, on_delete=models.CASCADE,default=1 )
  content = models.TextField(max_length=250)
  created_date = models.DateTimeField(auto_now_add=True)
  approved_comment = models.BooleanField(default=False)



  def approve(self):
    self.approved_comment = True
    self.save()
"""
  def __str__(self):
    return self.content
    #return '{}-{}'.format(self.listing.title, str(self.user.username))
"""
