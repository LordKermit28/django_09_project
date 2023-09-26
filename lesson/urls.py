from django.urls import path
from rest_framework.routers import DefaultRouter

from lesson.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView

app_name = 'lesson'

urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/list', LessonListAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-ret'),
    path('lesson/delete', LessonDestroyAPIView.as_view(), name='lesson-create'),
    path('lesson/update', LessonUpdateAPIView.as_view(), name='lesson-create'),
]
