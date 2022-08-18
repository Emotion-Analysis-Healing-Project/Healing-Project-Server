from django.urls import path, include
from api import views
from django.conf.urls import include

urlpatterns = [
    path('users', views.user_list),
    path('users/<int:pk>', views.user),
    path('login', views.login),
    path('asmr', views.asmr),
    path('video', views.video),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]
