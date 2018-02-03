from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns=[
   url(r'^signup/',views.register),
    #url(r'^login/',views.login),
]
