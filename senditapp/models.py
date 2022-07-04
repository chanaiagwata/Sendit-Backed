from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('profile_pic', blank=True)
    location = models.CharField(max_length=255, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

  
# class Destination(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name
    
class Parcel(models.Model):
    name = models.CharField(max_length=80)
    photo = CloudinaryField('parcel_pic', blank=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    weight = models.IntegerField()
    destination = models.CharField(max_length=100)
    # destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

