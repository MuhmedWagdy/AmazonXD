from django import forms


from .models import Course,Reviews


class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields = '__all__'

        




       
  





