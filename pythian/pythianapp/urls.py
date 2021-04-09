from django.contrib import admin
from django.urls import path,include
from pythianapp import views
urlpatterns = [
    path("",views.index,name="home"),
    path("result",views.result,name="result") 
]
