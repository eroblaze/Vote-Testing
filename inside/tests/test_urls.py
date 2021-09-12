from django.test import SimpleTestCase 
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.index = reverse("index")
        self.display = reverse("display")
        self.vote = reverse("vote")

    def test_index_url(self):
        the_resolved = resolve(self.index)

        self.assertEqual(the_resolved.func.__name__, "index")
        self.assertEqual(the_resolved.url_name, "index")

    def test_display_url(self):
        the_resolved = resolve(self.display)

        self.assertEqual(the_resolved.func.__name__, "display")
        self.assertIs(the_resolved.url_name, "display")

    def test_vote_url(self):
        the_resolved = resolve(self.vote)

        self.assertEqual(the_resolved.func.__name__, "vote")
        self.assertEqual(the_resolved.url_name, "vote")
