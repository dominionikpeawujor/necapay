from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('generate', views.generate, name='generate'),
    path('verify', views.verify, name='verify'),
]
