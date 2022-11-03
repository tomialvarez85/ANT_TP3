from django.test import TestCase, Client
from django.urls import reverse
from .models import Plan, Price


class PriceTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.plan_base = Plan.objects.create(name='Base')
        self.plan_pro = Plan.objects.create(name='Pro')
        Price.objects.create(plan=self.plan_base,
                             currency='ARS',
                             price=1)
        Price.objects.create(plan=self.plan_base,
                             currency='ARS',
                             price=2)
        Price.objects.create(plan=self.plan_base,
                             currency='ARS',
                             price=3)
        Price.objects.create(plan=self.plan_pro,
                             currency='ARS',
                             price=3)
        Price.objects.create(plan=self.plan_pro,
                             currency='USD',
                             price=3)

    def test_check_only_one_price(self):
        count_actives = Price.objects.filter(
            plan=self.plan_base,
            currency='ARS',
            active=True
        )
        self.assertEqual(count_actives.count(), 1)

    def test_check_plans(self):
        response = self.client.get(reverse('plans-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('currency'), 'ARS')
        self.assertEqual(len(response.data.get('plans')), 2)
