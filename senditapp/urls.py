from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileList.as_view()),
    path('destination/', views.DestinationList.as_view()),
    path('parcel/', views.ParcelList.as_view()),
    path('parcel/parcel-id/(?P<pk>[0-9]+)/',views.ParcelDescription.as_view())
]
