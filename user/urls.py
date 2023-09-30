from rest_framework.routers import DefaultRouter

from user.apps import UserConfig
from user.views import UserViewSet

app_name = UserConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [

    ] + router.urls