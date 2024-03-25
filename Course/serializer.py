from rest_framework import serializers
from .models import Course,Reviews
from django.db.models.aggregates import Avg




class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    # def get_avg_rate(self,product):
    #     avg = self.review_product.aggregate(rate_avg=Avg('rate'))
    #     if not avg['rate_avg']:
    #         result = 0
    #         return result
    #     return avg['rate_avg']








class ReviewSerializer(serializers.ModelSerializer):
    # avg_rate = serializers.SerializerMethodField()
    # course = CourseSerializer(source='course_categorie',many= True)
    class Meta:
        model = Reviews
        fields = '__all__'

    # def get_avg_rate(self,product):
    #     avg = self.review_product.aggregate(rate_avg=Avg('rate'))
    #     if not avg['rate_avg']:
    #         result = 0
    #         return result
    #     return avg['rate_avg']
        

class CourseDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(source='course_review',many=True)
    class Meta:
        model = Course
        fields = '__all__'

