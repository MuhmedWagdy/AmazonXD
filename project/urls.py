"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Course.views import all_course,course_detail,course_review,course_new,edit_course,delete_course,CourseList,CourseDetail,CreateCourse,Course_Update,DeleteCourse

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('course/', all_course),
    # path('course/<int:course_id>', course_detail),
    path('reviews/',course_review),
    # path('course/new',course_new),
    # path('course/<int:course_id>/edit',edit_course),
    # path('course/<int:course_id>/delete',delete_course),


    #CLASS BASED VIEWS
    path('course/', CourseList.as_view()),
    path('course/<int:pk>', CourseDetail.as_view()),
    path('course/new',CreateCourse.as_view()),
    path('course/<int:pk>/edit',Course_Update.as_view()),
    path('course/<int:pk>/delete',DeleteCourse.as_view()),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
