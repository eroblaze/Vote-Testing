from django.test import TestCase, Client
from inside.models import *
from django.urls import reverse


class TestCreateView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.index_url = reverse("index")

    def test_index_view_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")

    def test_index_view_POST(self):
        response = self.client.post(self.index_url, {
            "name": "The input"
        })
        query_set = Product.objects.all().count()
        first = Product.objects.first()

        self.assertEqual(response.status_code, 302)
        self.assertIs(query_set, 1)
        self.assertEqual(first.name, "The input")
        self.assertRedirects(
            response, reverse("display"), 
            msg_prefix="The expected isn't correct!"
        )


class TestDisplayView(TestCase):

    def setUp(self):
        self.client = Client()
        self.display_url = reverse("display")

        Product.objects.create(name="one")
        Product.objects.create(name="two")
        Product.objects.create(name="three")
    
    def test_display_view_GET(self):
        response = self.client.get(self.display_url)
        # Find out how to test if the function returns a context to the
        # Template
        values = Product.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "display.html")
        self.assertEqual(len(response.context['all']), 3)
        self.assertQuerysetEqual(
            response.context['all'], 
            values, 
            ordered=False
        )
        # This tests if the number of all objects passed to the template
        # Is equal to the number of available objects created.


class TestVoteView(TestCase):
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.vote = reverse("vote")
        self.product = Product.objects.create(name="queen")

    def test_vote_view_GET(self):
        response = self.client.get(self.vote)
        query_set = Product.objects.all().count()

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "vote.html")
        self.assertEqual(query_set, 1)
    
    def test_vote_view_POST(self):
        response = self.client.post(self.vote, {
            'p1': "vote"
        })
        the_one = Product.objects.first()

        self.assertEqual(the_one.vote, 1)
        self.assertEqual(response.status_code, 302)
