from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from prices.models import Plan, Price
from prices.serializers import PlanSerializer


class ListPlans(GenericViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    authentication_classes = []
    permission_classes = []

    def list(self, request, format=None):
        currency = request.GET.get('currency', 'ARS')
        queryset = Price.objects.exclude(active=False).filter(currency=currency).values(
            'price', 'plan_id', 'plan__name', 'plan__description'
        )
        serializer = PlanSerializer(data=queryset)
        data = {'currency': currency, 'plans': serializer.initial_data}
        return Response(data)
