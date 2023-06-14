from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listElement.urls')),
    path('comment/', include('comment.urls')),
]