from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from user import views,adduser,getuser,login
urlpatterns = [
    # url(r'^login', views.login),
    url(r'^adduser', adduser.add),
    url(r'^getuser', getuser.get),
    url(r'^login/$', login.login),
]