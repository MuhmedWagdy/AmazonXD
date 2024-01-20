from django.db import models

# Create your models here.

catgorey_name = [('software_test','software_test'),('devoloper','devoloper'),('Data_Analysis','Data_Analysis')]




class Course(models.Model):
    name= models.CharField(max_length=200,blank=True, null=True)
    subtitle=models.name = models.CharField(max_length=300,blank=True, null=True)
    price = models.FloatField(max_length=10)
    category=models.Choices(catgorey_name)
    



class reviews(models.Model):
    name = ''

    

