from django import forms

from .models import Course,Reviews


class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields = '__all__'
        # exclude = ('user',)


class ReviewForm(forms.ModelForm):

    class Meta:
         
         model= Reviews
         fields = ['review']


   





       
  





