from django.db import models

from django.contrib.auth import User

from django.utils import timezone


# Create your models here.

catgorey_name = [('software_test','software_test'),('devoloper','devoloper'),('Data_Analysis','Data_Analysis')]

class Course(models.Model):
    name= models.CharField(max_length=200,blank=True, null=True)
    subtitle=models.name = models.CharField(max_length=300,blank=True, null=True)
    discription = models.TextField(max_length= 1000)
    price = models.FloatField(max_length=10)
    category=models.Choices(catgorey_name)



    def __str__(self):
        return self.name
    

class Reviews(models.Model):
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, related_name='courses_review', on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.user}  {self.course}'

