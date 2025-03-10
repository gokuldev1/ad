from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    
    path('',views.index,name='index'),
   path("send-email", views.send_email, name="send_email"),
]
