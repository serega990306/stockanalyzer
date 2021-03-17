from rest_framework import routers
from .views import StockListView, SectorListView, StockHistoryView

router = routers.SimpleRouter()
router.register(r'sector', SectorListView)
router.register(r'stock', StockListView)
router.register(r'stock_hist', StockHistoryView)
urlpatterns = router.urls
