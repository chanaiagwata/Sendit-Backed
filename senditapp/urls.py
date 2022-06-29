from django.urls import path
from . import views

urlpatterns = [
    path(r'^api/profile/$', views.ProfileList.as_view()),
    path(r'^api/destination/$', views.DestinationList.as_view()),
    path(r'^api/parcel/$', views.ParcelList.as_view())
]
