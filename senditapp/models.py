from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
 
class Admin(models.Model):
    user = models.OneToOneField(User, related_name='admin', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
    
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return str(self.user.username)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('profile_pic', blank=True)
    location = models.CharField(max_length=255, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class ParcelStatus(models.Model): 
    status = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Parcel Status {self.status}'

    
class Parcel(models.Model):
    name = models.CharField(max_length=80)
    photo = CloudinaryField('parcel_pic', blank=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    weight = models.IntegerField()
    parcel_status = models.ForeignKey(ParcelStatus, on_delete=models.SET_NULL, blank=True, null=True)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-pk"]

    def save_parcel(self):
        self.save()

    def delete_parcel(self):
        self.delete()