from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data_category = Category.objects.create(name='str-test_name', slug='str-test_slug')

    def test_category_model_entry(self):
        """
        тестируем данные категории
        """
        data = self.data_category
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'str-test_name')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='str_name', slug='str_slug')
        User.objects.create(username='admin')
        self.data_product_default = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.000', image='django')
        self.data_product_no_active = Product.objects.create(category_id=1, title='django advanced', created_by_id=1,
                                            slug='django-advanced', price='20.00', image='django', is_active=False)
    def test_products_model_entry(self):
        data = self.data_product_default
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')