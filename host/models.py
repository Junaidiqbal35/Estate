from django.db import models
from datetime  import  datetime
from  django.contrib.auth.models import User

# Create your models here.



class Host ( models.Model ):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)


    name = models.CharField(max_length=45)
    phone = models.CharField ( max_length=20 )
    photo = models.ImageField ( upload_to='photos/%Y/%m/%d/',blank=True )
    description = models.TextField ( blank=True )
    is_mvp = models.BooleanField(default=False)

    hire_date = models.DateTimeField ( default=datetime.now, blank=True)
    def __str__(self):
        return self.name
