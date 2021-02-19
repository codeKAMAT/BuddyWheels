from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.about, name='contact'),
    path('booking', views.booking, name='booking'),
]