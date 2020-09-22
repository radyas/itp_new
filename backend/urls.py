from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)
router.register(r'api/orders', views.OrderViewSet)
router.register(r'api/customers', views.CustomerViewSet)
router.register(r'api/provider', views.ProviderViewSet)
router.register(r'api/branch', views.BranchViewSet)
router.register(r'api/delivery', views.DeliveryViewSet)
router.register(r'api/voucher', views.VoucherViewSet)
router.register(r'api/attendance', views.AttendanceViewSet)
router.register(r'api/adjustment', views.AdjustmentsViewSet)
router.register(r'api/salary', views.SalaryViewSet)
router.register(r'api/designation', views.DesignationViewSet)
router.register(r'api/department', views.DepartmentViewSet)
router.register(r'api/documents', views.DocumentsViewSet)
router.register(r'api/Product', views.ProductViewSet)
router.register(r'api/Supplier', views.SupplierViewSet)
router.register(r'api/Warehouse', views.WarehouseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
