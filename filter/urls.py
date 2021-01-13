from rest_framework import routers
from .views import FilterFeedViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'filter', FilterFeedViewSet, basename="filter")
urlpatterns = router.urls

# urlpatterns = [
    # path('filter', FilterList.as_view(), name="filter-list")
# ]

