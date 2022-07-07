from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.getRoutes),
    path('api/admin',views.AdminSignUpView.as_view()),
    path('api/client',views.ClientSignUpView.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/parcel', views.ParcelList.as_view()),
    path('api/parcel/<int:pk>',views.ParcelDescription.as_view()),
    path('api/api-token-auth', obtain_auth_token ,name='api_token_auth'),
    path('api/login', LoginView.as_view()),
    path('api/logout', LogoutView.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)