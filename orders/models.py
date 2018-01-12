from django.db import models


class Order(models.Model):
    size = models.DecimalField(max_digits=5, decimal_places=2)
    customer_name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
