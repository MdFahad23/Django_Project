from django.contrib import admin
from django.urls import path
from First_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home)
]
