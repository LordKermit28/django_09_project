from rest_framework import serializers

from lesson.models import Lesson


class LessonSerializer(serializers.Serializer):
    class Meta:
        model = Lesson
        fields = '__all__'
