from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CourseSerializer

from .models import Course


@api_view(['GET'])
def course_list_api(request):
    course = Course.objects.all()         #list all Course 
    data = CourseSerializer(course,many=True).data      #json 
    return Response({'course':data})                  



    

