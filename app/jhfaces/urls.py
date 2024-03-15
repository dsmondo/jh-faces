from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('stationInfo.urls')),
    path('stationInfo/', include('stationInfo.urls')),
    path('admin/', admin.site.urls),
]
