from rest_framework import serializers
from orders.models import Order as OrderModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['id', 'size', 'customer_name', 'address', 'created']
        read_only_fields = ('id',)
