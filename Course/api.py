from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CourseSerializer

from .models import Course


@api_view(['GET'])
def course_list_api(request):
    course = Course.objects.all()[:15]        #list all Course 
    data = CourseSerializer(course,many=True,context={'request':request}).data      #json 
    return Response({'course':data})                  



@api_view(['GET'])
def course_detail_api(request,course_id):
    course = Course.objects.get(id=course_id)        #list all Course 
    data = CourseSerializer(course,context={'request':request}).data      #json 
    return Response({'course':data})   


    

