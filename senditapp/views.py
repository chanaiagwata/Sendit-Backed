from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializer import *
from .permissions import IsAdminOrReadOnly

# Create your views here.

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
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
        permission_classes = (IsAdminOrReadOnly,)
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
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ParcelDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_parcel(self,pk):
        try:
            return Parcel.objects.get(pk=pk)
        except Parcel.DoesNotExist:
            return Http404
    def get(self, request, pk, format=None):
        parcel = self.get_parcel(pk)
        serializers = ParcelSerializer(parcel)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        parcel = self.get_parcel(pk)
        serializers = ParcelSerializer(parcel, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        parcel = self.get_parcel(pk)
        parcel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)