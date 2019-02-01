from django.urls import path
from . import views

urlpatterns = [
    path('', views.fontend, name="fontend"),
    path('contact/', views.contact, name="contact"),
    path('term/', views.term, name="term"),
]