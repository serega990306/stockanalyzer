from rest_framework import routers
from .views import StockView, SectorView, StockHistoryView, SectorStockView

router = routers.SimpleRouter()
router.register(r'sector', SectorView)
router.register(r'sector_stock', SectorStockView)
router.register(r'stock', StockView)
router.register(r'stock_hist', StockHistoryView)
urlpatterns = router.urls
