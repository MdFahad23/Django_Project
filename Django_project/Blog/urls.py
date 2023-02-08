from django.urls import path
from . import views

urlpatterns = [
    path("blog1/", views.Blog)
]
