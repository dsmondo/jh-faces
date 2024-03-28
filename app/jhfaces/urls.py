from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('stationInfo.urls')),
    path('stationInfo/', include('stationInfo.urls')),
    path('marketTools/', include('marketTools.urls')),
    path('admin/', admin.site.urls),
]
