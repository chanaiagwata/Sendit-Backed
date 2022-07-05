from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .models import *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from django.contrib.auth import get_user_model
import jwt, datetime
from rest_framework import generics
from rest_framework.decorators import api_view

User = get_user_model()

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/admin',
        'api/client',
        'api/profile',
        'api/parcel',
        'api/parcel/<int:pk>',
        'api/login',
        'api/logout',
    ]
    return Response(routes)


class AdminSignUpView(generics.GenericAPIView):
    serializer_class = AdminSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': 'account created successfully'
        }
        return Response(context)


class ClientSignUpView(generics.GenericAPIView):
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': 'account created successfully'
        }
        return Response(context)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token
        }
        return response
   
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout Successful'
        }
        return response
    
        
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
            return Parcel.objects.get(id=pk)
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