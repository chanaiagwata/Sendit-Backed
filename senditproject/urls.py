from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('senditapp.urls')),
    path('api-token-auth/', obtain_auth_token),

]
