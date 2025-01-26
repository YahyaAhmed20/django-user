from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE,blank=True, null=True)
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    image=models.ImageField(upload_to='profile/')
    
    def __str__(self):
           return str(self.user)
       
       
class City(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
           return (self.name)
              