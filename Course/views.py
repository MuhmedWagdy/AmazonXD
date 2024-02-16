from django.shortcuts import render ,redirect

# Create your views here.

from .models import Course,Reviews
from .forms import CourseForm,ReviewForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView



# def review_detail(request,pk):
#     data = Reviews.objects.get(id=pk)

#     form = ReviewForm()
#     return render(request,'Course/reviews_course.html',{'data':data,'form':form})



#function based views
def all_course(request):
    data = Course.objects.all()
    return render(request,'Course/course_list.html',{'data':data})

#class based views

class CourseList(ListView):
    model= Course

# ==============================================================================================================================================================================
#function based views
def course_detail(request,pk):
    data = Course.objects.get(id=pk)
    course_review = Reviews.objects.filter(course=data)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user= request.user
            myform.review = data
            myform.save()
    else:

       form = ReviewForm()
    return render(request,'Course/course_detail.html',{'data':data,'form':form,'course_review':course_review})


#class bassed views
class CourseDetail(DetailView):
    model= Course

#==================================================================================================================================================================================

class CreateCourse(CreateView):
    model = Course
    fields=['name','subtitle','discription','price','categorie']
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
    return render(request,'Course/course_form.html',{'form':form})


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Course_Update(UpdateView):
    model= Course
    fields=['name','subtitle','discription','price','category']
    success_url='/course'
    template_name='Course/Course_update.html'


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_course(request,course_id):
    data = Course.objects.get(id=course_id)
    data.delete()
    return redirect('/course')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class DeleteCourse(DeleteView):
    model =  Course
    success_url='/course'






   



    

