from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'provider', views.ProviderViewSet)
router.register(r'branch', views.BranchViewSet)
router.register(r'delivery', views.DeliveryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
