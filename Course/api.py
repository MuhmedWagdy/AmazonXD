from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CourseSerializer

from .models import Course



def course_list_api(request):
    course = Course.objects.all()         #list all Course 
    data = CourseSerializer(course).data                      #json 



    

