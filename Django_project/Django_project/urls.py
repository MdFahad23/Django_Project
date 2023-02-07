from django.contrib import admin
from django.urls import path

from Home import views
from Blog import views as b

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('blog/', b.Blog)
]
