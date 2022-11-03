from django.db import models
from django.core.validators import MinValueValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        app_label = 'prices'


class Plan(TimeStampedModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)


class Price(TimeStampedModel):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3)
    price = models.FloatField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        if self.active:
            Price.objects.filter(
                plan=self.plan, currency=self.currency
            ).update(active=False)
        super().save(*args, **kwargs)
