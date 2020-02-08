from django.contrib import admin
from django.urls import include, path
from libraryapp.models import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libraryapp.urls')),
]
