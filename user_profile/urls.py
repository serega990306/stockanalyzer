from rest_framework import routers
from .views import UserProfileView

router = routers.SimpleRouter()
router.register(r'profile', UserProfileView)
urlpatterns = router.urls
