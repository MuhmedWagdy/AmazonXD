from django.contrib import admin
from django.urls import path
from .api import course_list_api,course_detail_api,CourseListAPI,CourseDetailAPI,review_list_api



urlpatterns = [
    # path('api/list' , course_list_api),
    # path('api/list/<int:course_id>' , course_detail_api),

    path('api/list' , review_list_api),
    path('api/list' , CourseListAPI.as_view()),
    path('api/list/<int:pk>' , CourseDetailAPI.as_view()),


]
