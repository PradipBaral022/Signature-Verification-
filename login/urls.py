from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user,name='login'),
    path('home',views.home,name='home'),
    #path('Verification',views.makeVerification,name='verify'),
    path('upload',views.upload_verfiy,name='upload'),
]