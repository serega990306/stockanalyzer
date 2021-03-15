from rest_framework import routers
from .views import StockListView, SectorListView

router = routers.SimpleRouter()
router.register(r'sector', SectorListView)
router.register(r'stock', StockListView)
urlpatterns = router.urls
