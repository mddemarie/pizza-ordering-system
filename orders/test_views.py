from rest_framework import status
from rest_framework.test import APITestCase

from orders.models import Order

class OrderTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = '/api/orders/'

        # create a data for POST method
        cls.order_post = {
            "size": 150,
            "customer_name": "Marie",
            "address": "Innstrasse 7, 12045 Berlin"
            }

        # create a order data for GET method
        cls.order_get = {
            "id": 1,
            "size": 150,
            "customer_name": "Marie",
            "address": "Innstrasse 7, 12045 Berlin",
            "created": "2018-01-10T20:29:42.738368Z"
            }

        cls.order_get2 = {
            "id": 2,
            "size": 50,
            "customer_name": "Jane",
            "address": "Barbal-str. 5, 19738 Berlin",
            "created": "2018-01-11T00:12:49.329155Z"
            }

        # create 2 instances of feedback for GET method
        cls.order = Order.objects.create(**cls.order_get)
        Order.objects.create(**cls.order_get2)

        cls.order_url = cls.url + str(cls.order.id) + '/'
  
    # testing a POST method
    def test_create_order_works_as_non_user(self):
        """
        Non-User is allowed to create a pizza order.
        """
        response = self.client.post(self.url, self.order_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
    def test_create_order_fails_without_pizza_size(self):
        """
        Size field cannot be empty.
        """
        response = self.client.post(
            self.url, {k: v for (k, v) in self.order_post.items() if k is not 'size'}
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data['size'], ['This field is required.'])

    def test_create_order_fails_without_customer_name(self):
        """
        Customer name field cannot be empty.
        """
        response = self.client.post(self.url, {k: v for (k, v) in self.order_post.items() if k is not 'customer_name'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data['customer_name'], ['This field is required.'])

    def test_create_order_fails_without_address(self):
        """
        Address field cannot be empty.
        """
        response = self.client.post(self.url, {k: v for (k, v) in self.order_post.items() if k is not 'address'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data['address'], ['This field is required.'])

    # testing a GET method
    def test_list_orders_works_as_non_user(self):
        """
        Non-User is allowed to see list of pizza orders.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 2)
    
    # testing a PATCH method
    def test_modify_order_works_as_non_user(self):
        """
        Non-user is allowed to change a pizza order.
        """
        response = self.client.patch(self.order_url, {'size': 100}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data['size'], '100.00')

    # testing a DELETE method
    def test_remove_order_works_as_non_user(self):
        """
        Non-user is allowed to change a pizza order.
        """
        response = self.client.delete(self.order_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)
