from django.urls import path 
from django.urls.conf import include
from .views import home
from . import views



urlpatterns = [
    path('', home, name='index' ),

]