from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LoginView, UserView, LogoutView


urlpatterns = [
    path('profile/', views.ProfileList.as_view()),
    path('parcel', views.ParcelList.as_view()),
    path('parcel/<int:pk>',views.ParcelDescription.as_view()),
    path('api-token-auth', obtain_auth_token ,name='api_token_auth'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

]
