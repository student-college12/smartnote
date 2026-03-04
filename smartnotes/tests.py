from django.test import TestCase
from django.urls import reverse


class URLTests(TestCase):
    def test_register_url_exists(self):
        """Reverse lookup for the registration view must resolve."""
        url = reverse('smartnotes:register')
        self.assertEqual(url, '/smartnotes/register/')

    def test_login_url_exists(self):
        url = reverse('smartnotes:login')
        self.assertEqual(url, '/smartnotes/login/')

# Create your tests here.
