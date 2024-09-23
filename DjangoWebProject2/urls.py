"""
Definition of urls for DjangoWebProject2.
"""

from django.urls import path
from django.contrib import admin
from MyApp1 import views
from django.views.generic import RedirectView

urlpatterns = [
    path ('',views.main),  
    path ('about', views.about),
    path ('uslugi',views.uslugi) ,
    path ('direction.html',views.direction), 
    path ('contact.html',views.contact), 
    path ('server', views.server),
    path ('product', views.product),
    path ('service', views.service),
    path ('its', views.its),
    path ('base', views.base),
    path ('prof', views.prof),
    path ('LK', views.LK),
]
