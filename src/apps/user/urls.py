from apps.user.api.views import UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('', UserViewSet, 'users')

urlpatterns = []
urlpatterns += router.urls
