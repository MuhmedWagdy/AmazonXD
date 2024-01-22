from django.shortcuts import render ,redirect

# Create your views here.

from .models import Course,Reviews
from .forms import CourseForm
from django.views.generic import ListView,DetailView,CreateView


#function based views
def all_course(request):
    data = Course.objects.all()
    return render(request,'Course/course_list.html',{'data':data})

#class based views

class CourseList(ListView):
    model= Course

# ==============================================================================================================================================================================
#function based views
def course_detail(request,course_id):
    data = Course.objects.get(id=course_id)
    return render(request,'Course/course_detail.html',{'data':data})


#class bassed views
class CourseDetail(DetailView):
    model= Course

#==================================================================================================================================================================================

class CreateCourse(CreateView):
    model = Course
    fields=['name','subtitle','discription','price','category']

    success_url='/course'















def course_review(request):


    review = Reviews.objects.all()

    return render(request,'Course/reviews_course.html',{'review':review})


def course_new(request):
    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            myform= form.save(commit=False)
            myform.save()
            return redirect('/course')
    else:
        form=CourseForm()

    return render(request,'Course/new_course.html',{'form':form})



def edit_course(request,course_id):
      data = Course.objects.get(id=course_id)
      if request.method=='POST':
        form = CourseForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform= form.save(commit=False)
            myform.save()
            return redirect('/course')
      else:
        form=CourseForm(instance=data)
      return render(request,'Course/edit_course.html',{'form':form})


  

def delete_course(request,course_id):
    data = Course.objects.get(id=course_id)
    data.delete()
    return redirect('/course')

   



    

