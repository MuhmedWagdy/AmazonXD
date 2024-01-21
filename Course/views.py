from django.shortcuts import render

# Create your views here.

from .models import Course,Reviews



def all_course(request):

    data = Course.objects.all()
    return render(request,'course_list.html',{'data':data})



def course_detail(request,course_id):
    data = Course.objects.get(id=course_id)
    return render(request,'course_detail.html',{'data':data})

    

