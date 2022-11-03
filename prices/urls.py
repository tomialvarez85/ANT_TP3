from rest_framework import routers
from prices.views import ListPlans

price_router = routers.DefaultRouter()
urlpatterns = [

]
price_router.register(r'plans', ListPlans, 'plans')

urlpatterns += price_router.urls