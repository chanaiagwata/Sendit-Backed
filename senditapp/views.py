from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializer import *

# Create your views here.

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DestinationList(APIView):
    def get(self, request, format=None):
        all_destination = Destination.objects.all()
        serializers = DestinationSerializer(all_destination, many=True)
        
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ParcelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ParcelList(APIView):
    def get(self, request, format=None):
        all_parcel = Parcel.objects.all()
        serializers = ParcelSerializer(all_parcel, many=True)
        
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ParcelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)