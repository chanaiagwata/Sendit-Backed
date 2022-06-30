from dataclasses import fields
from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'profile_pic', 'location', 'date_created')
        
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('id','name')
        
class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ('id','name', 'description', 'price','weighted')