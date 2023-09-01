from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.home_url = reverse('home')
        self.about_us = reverse('about')

        return super().setUp()
    
class RenderPagesTest(BaseTest):
    def test_can_view_home_page_correctly(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_can_view_about_us_page_correctly(self):
        response = self.client.get(self.about_us)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')