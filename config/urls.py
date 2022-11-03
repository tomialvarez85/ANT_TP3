
from django.contrib import admin
from django.urls import path
from prices.urls import price_router
from coupons.urls import coupons_router
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coupons.urls')),
    path('', include('prices.urls')),
]

