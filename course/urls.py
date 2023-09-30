from django.urls import path
from rest_framework.routers import DefaultRouter
from course.apps import CourseConfig
from course.views import CourseViewSet, PayingListView, PayingCreateView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [

    path('paying/', PayingListView.as_view(), name='paying-list'),
    path('paying/create/', PayingCreateView.as_view(), name='paying-create')

    ] + router.urls