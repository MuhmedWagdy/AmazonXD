from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CourseSerializer,ReviewSerializer
from rest_framework import generics
from .models import Course ,Reviews


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


class CourseListAPI(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class CourseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@api_view(['GET'])
def review_list_api(request):
    course = Reviews.objects.all()[:15]        #list all Course 
    data = ReviewSerializer(course,many=True,context={'request':request}).data      #json 
    return Response({'course':data})                  


@api_view(['GET'])
def review_list_api(request,course_id):
    course = Reviews.objects.get(id=course_id)        #list all Course 
    data = ReviewSerializer(course,many=True,context={'request':request}).data      #json 
    return Response({'course':data})   



class ReviewListAPI(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







    

