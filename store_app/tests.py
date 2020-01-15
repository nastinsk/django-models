from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Product


class StoreTests(TestCase):

    def setUp(self):
        self.manufacturer = get_user_model().objects.create_user(username = "test_user", email = 'test_user@gmail.com', password="password")

        self.product = Product.objects.create(title = "piroshky", description = "loremipsum text lalala", manufacturer = self.manufacturer)

    def test_string_representation(self):

        product = Product.objects.get(id=1)

        self.assertEqual(str(product), 'piroshky' )

