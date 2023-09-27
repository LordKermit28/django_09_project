from django.urls import path

from lesson.views import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView

app_name = 'lesson'


urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
]
