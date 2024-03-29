from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('stationInfo/', include('stationInfo.urls')),
    path('marketTools/', include('marketTools.urls')),
    path('admin/', admin.site.urls),
]
