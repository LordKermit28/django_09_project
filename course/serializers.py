from django.shortcuts import get_object_or_404
from rest_framework import serializers

from course.models import Course, Paying
from lesson.serializers import LessonSerializer
from user.models import User


class PayingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paying
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    paying = PayingSerializer(many=True)

    def get_lessons(self, instance):
        lessons = instance.lesson_set.all()
        lesson_serializer = LessonSerializer(lessons, many=True)
        return lesson_serializer.data
    def create(self, validated_data):
        paying_data = validated_data.pop('paying')
        course = Course.objects.create(**validated_data)

        for payment in paying_data:
            user = get_object_or_404(User, email=payment['user'])
            Paying.objects.create(user=user, sum=payment['sum'], method_to_pay=payment['method_to_pay'], course=course)

        return course


    class Meta:
        model = Course
        fields = '__all__'

