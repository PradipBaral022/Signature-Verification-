from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user,name='login'),
    path('logout_user',views.logout_user,name='logout'),
    # path('home',views.home,name='home'),
    #path('Verification',views.makeVerification,name='verify'),
    path('home',views.upload_verfiy,name='home'),
]