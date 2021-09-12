from django.test import TestCase
from django.urls import reverse
from inside.models import Product


class TestModels(TestCase):

    def setUp(self):
        self.first = Product.objects.create(
            name="database"
        )

    def test_if_str_returns_name(self):
        self.assertIs(self.first.__str__(), "database")