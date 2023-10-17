from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import generics

from course.models import Course, Paying
from course.permissions import CoursePermission
from course.serializers import CourseSerializer, PayingSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [CoursePermission]

    def perform_create(self, serializer):
        new_course = serializer.save(author=self.request.user)


class PayingListView(generics.ListAPIView):
    serializer_class = PayingSerializer
    queryset = Paying.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'method_to_pay',)
    ordering_fields = ('date_to_pay',)

class PayingCreateView(generics.CreateAPIView):
    serializer_class = PayingSerializer
