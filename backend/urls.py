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
router.register(r'voucher', views.VoucherViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'adjustment', views.AdjustmentsViewSet)
router.register(r'salary', views.SalaryViewSet)
router.register(r'designation', views.DesignationViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'documents', views.DocumentsViewSet)
router.register(r'Product', views.ProductViewSet)
router.register(r'Supplier', views.SupplierViewSet)
router.register(r'Warehouse', views.WarehouseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/authUser/', views.ListUsers.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
