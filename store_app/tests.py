from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Product
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_home_page_status_check(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

class StoreModelTests(TestCase):

    def setUp(self):
        self.manufacturer = get_user_model().objects.create_user(username = "test_user", email = 'test_user@gmail.com', password="password")

        self.product = Product.objects.create(title = "piroshky", description = "loremipsum text lalala" , manufacturer = self.manufacturer)

    def test_string_representation(self):

        product = Product.objects.get(id=1)

        self.assertEqual(str(product), 'piroshky' )

    def test_product_description(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.description, "loremipsum text lalala" )


class ProductDetailPageTests(TestCase):

    def setUp(self):
        self.manufacturer = get_user_model().objects.create_user(username = "test_user", email = 'test_user@gmail.com', password="password")

        self.product = Product.objects.create(title = "piroshky", description = "loremipsum text lalala" , manufacturer = self.manufacturer)

    def test_model_contains(self):
        self.assertEqual(f'{self.product.title}', 'piroshky')
        self.assertEqual(f'{self.product.manufacturer}', 'test_user')
        self.assertEqual(f'{self.product.description}', 'loremipsum text lalala')

    def test_product_detail_page_status_check(self):
        product = Product.objects.get(id=1)

        url = reverse('product_detail', kwargs={"pk":product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_template(self):
        product = Product.objects.get(id=1)

        url = reverse('product_detail', kwargs={"pk":product.id})
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertTemplateUsed(response, 'base.html')
