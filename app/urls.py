from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = router.urls