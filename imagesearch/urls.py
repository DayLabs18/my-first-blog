from django.urls import path
from . import views


urlpatterns = [
    path('', views.search_upload, name='search_upload'),
]