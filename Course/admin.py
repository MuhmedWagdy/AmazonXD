from django.contrib import admin

# Register your models here.
from .models import Course,Reviews
admin.site.register(Course)
admin.site.register(Reviews)
