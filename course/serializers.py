from django.shortcuts import get_object_or_404
from rest_framework import serializers

from course.models import Course, Paying
from lesson.models import Lesson
from user.models import User


class PayingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paying
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    paying = PayingSerializer(many=True)
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['name', 'preview', 'description', 'lesson_count', 'paying']

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def create(self, validated_data):
        paying_data = validated_data.pop('paying')
        lessons_data = self.initial_data.get('lessons', [])

        course = Course.objects.create(**validated_data)

        for lesson_id in lessons_data:
            lesson = get_object_or_404(Lesson, id=lesson_id)
            course.lessons.add(lesson)

        for payment in paying_data:
            user = get_object_or_404(User, email=payment['user'])
            Paying.objects.create(user=user, sum=payment['sum'], method_to_pay=payment['method_to_pay'], course=course)

        return course