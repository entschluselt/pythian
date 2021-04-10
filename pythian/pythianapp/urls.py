from django.contrib import admin
from django.urls import path,include
from pythianapp import views
urlpatterns = [
    path("",views.index,name="home"),
    path("result",views.result,name="result"), 
    path("appointment",views.appointment,name="appointment"), 
    path("about",views.about,name="about"), 
    path("nearby",views.nearby,name="nearby"), 
    path("emergency",views.emergency,name="emergency") 
    
]
