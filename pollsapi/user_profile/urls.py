from django.urls import path

from .views import Home

urlpatterns = [
    path('acl/', Home.as_view(), name='acl'),
]