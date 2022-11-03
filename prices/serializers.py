from rest_framework import serializers, fields


class PlanSerializer(serializers.Serializer):
    id = fields.IntegerField(source='plan_id')
    name = fields.CharField(source='plan__name')
    description = fields.CharField(source='plan__description')
    price = fields.FloatField()
