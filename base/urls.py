from django.urls import path
from django.http import HttpResponse
from . import views  

urlpatterns = [
    path("", views.home, name="home"), 
    path("predict/", views.predict, name="predict"), 
    path("analysis/", views.analysis, name="analysis"), 
]