from django.contrib import admin

# Register your models here.   
from .models import Course,Reviews,Categories
admin.site.register(Course)
admin.site.register(Reviews)
admin.site.register(Categories)
