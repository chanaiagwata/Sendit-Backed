from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileList.as_view()),
    path('destination/', views.DestinationList.as_view()),
    path('parcel/', views.ParcelList.as_view())
]
