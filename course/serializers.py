from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        preview = self.context['request'].data.get('preview')
        course = Course.objects.create(preview=preview, **validated_data)
        return course
