from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from .models import Product


class ProductTestModel(APITestCase):
    def setUp(self):
        self.product = mommy.make(Product)
        self.client = APIClient()

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))
        self.assertEquals(self.product.__str__(), self.product.name)

    def test_api_get(self):
        url = reverse('api:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)        