from rest_framework import routers
from coupons.views import ListCoupons

coupons_router = routers.DefaultRouter()
urlpatterns = [

]

coupons_router.register(r'coupons', ListCoupons, 'coupons')
urlpatterns += coupons_router.urls