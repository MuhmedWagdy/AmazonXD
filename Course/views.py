from django.shortcuts import render ,redirect

# Create your views here.

from .models import Course,Reviews
from .forms import CourseForm



def all_course(request):

    data = Course.objects.all()
    return render(request,'course_list.html',{'data':data})



def course_detail(request,course_id):
    data = Course.objects.get(id=course_id)
    return render(request,'course_detail.html',{'data':data})





def course_review(request):


    review = Reviews.objects.all()

    return render(request,'reviews_course.html',{'review':review})


def course_new(request):
    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/course')
    else:
        form = CourseForm()

    return render(request,'new_course.html',{'form':form})



def edit_course(request,course_id):

    pass

def delete_course(request,course_id):
    pass



    

