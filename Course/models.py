from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager



# Create your models here.
FLAG_TYPES = (
    ('software_test','software_test'),
    ('devoloper','devoloper'),
    ('Data_Analysis','Data_Analysis'),
)


# categories_name = (
#     ("development","development"),
#     ("Design","Design"),
#     ("It","It"),
#     ("Marketing","Marketing"),
# )

class Categories(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name= models.CharField(max_length=200,blank=True, null=True)
    subtitle= models.name = models.CharField(max_length=300,blank=True, null=True)
    discription = models.TextField(max_length= 1000)
    price = models.FloatField(max_length=10)
    # category=models.CharField(choices= FLAG_TYPES,max_length=20)
    categorie = models.ForeignKey(Categories , related_name="course_categorie" , on_delete=models.CASCADE,null=True)
    tags = TaggableManager()
    

    def __str__(self):
        return  f'{self.name}'
    


    
class Reviews(models.Model):
    # User maybe comment review  Use SET_NULL
    user = models.ForeignKey(User, related_name='user_review', on_delete=models.SET_NULL, null=True,blank=True)
    course = models.ForeignKey(Course, related_name='course_review', on_delete=models.CASCADE,null=True,blank=True)
    review = models.TextField(max_length=400)
    rate = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user}  {self.course}'

