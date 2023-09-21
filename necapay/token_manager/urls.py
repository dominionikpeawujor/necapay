from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('generate', views.generate, name='generate'),
    path('verify', views.verify, name='verify'),
]
