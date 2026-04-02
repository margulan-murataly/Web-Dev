from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = router.urls
 