from django.contrib import admin
from django.urls import path

from .api import course_list_api



urlpatterns = [

    path('api/list' , course_list_api),



    
]
