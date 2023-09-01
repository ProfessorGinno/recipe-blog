from django.test import TestCase
from django.urls import reverse
from ..models import Post
from django.core.files.uploadedfile import SimpleUploadedFile

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.index_url = reverse('blog_index')
        self.create_post_url = reverse('create_post')
        self.recipe = {
            'title': 'Recipe',
            'description': 'Recipe long description',
            'recipe_country': 'Colombia',
        }
        self.user = {
            'username': 'test_username_pass',
            'password1': 'password.123',
            'password2': 'password.123'
        }

        return super().setUp()
    
class ViewPagesTest(BaseTest):
    def test_can_view_blog_index_page_correctly(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes_blog/index_post.html')

class PostTest(BaseTest):
    def test_can_create_blog_correctly(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.login(username='test_username_pass', password='password.123')
        response = self.client.get(self.create_post_url, self.recipe, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes_blog/create_post.html')
        response = self.client.post(self.create_post_url, self.recipe, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_can_view_detail_page_correctly(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.login(username='test_username_pass', password='password.123')
        response = self.client.post(self.create_post_url, self.recipe, format='text/html')
        post=Post.objects.filter(title=self.recipe['title']).first()
        url = reverse('detail_post', args=[post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)