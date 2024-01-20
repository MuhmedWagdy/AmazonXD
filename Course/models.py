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
    



class reviews(models.Model):
    name = models.ForeignKey(Course,on_delete= models.CASCADE, related_name='reviews')



