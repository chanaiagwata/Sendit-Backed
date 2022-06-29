from dataclasses import fields
from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'location', 'date_created')
        
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('name')
        
class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ('name', 'description', 'price','weighted', 'destination')