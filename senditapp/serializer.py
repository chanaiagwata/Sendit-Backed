from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'user', 
            'profile_pic', 
            'location', 
            'date_created'
            )
        
        
class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = (
            'id',
            'name', 
            'description',
            'price',
            'weight',
            'destination'
            )
        
