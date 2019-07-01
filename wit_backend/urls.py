from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('user', include('user.urls')),
    path('train', include('train.urls')),
    path('admin/', admin.site.urls)
]