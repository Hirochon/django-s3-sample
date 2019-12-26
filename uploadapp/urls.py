from django.urls import path
from . import views

urlpatterns = [
    path('', views.Photo.as_view()),
]