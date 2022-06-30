from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic', blank=True)
    location = models.CharField(max_length=255, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
  
class Destination(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Parcel(models.Model):
    name = models.CharField(max_length=80)
    photo = CloudinaryField('parcel_pic', blank=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    weighted = models.IntegerField()
    # destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

