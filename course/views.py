from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from course.models import Course
from course.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

