from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from orders.models import Order as OrderModel
from orders.serializers import OrderSerializer

class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
