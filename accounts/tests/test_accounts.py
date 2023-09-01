from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('signup')
        self.sign_up_page_success_url = reverse('sign_up_success')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.update_url = reverse('update_user')
        self.user = {
            'username': 'test_username_pass',
            'password1': 'password.123',
            'password2': 'password.123'
        }

        self.user_update = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@email.com',
            'phone': '555555555',
            'address': 'address',
            'country': 'Colombia',
        }
        
        self.user_short_password = {
            'username': 'test_username',
            'password1': 'pass',
            'password2': 'pass'
        }
        self.user_similar_username = {
            'username': 'test_username',
            'password1': 'test_username',
            'password2': 'test_username'
        }
        self.user_only_numbers = {
            'username': 'test_username',
            'password1': '123456789',
            'password2': '123456789'
        }
        self.user_not_matching_passwords = {
            'username': 'test_username',
            'password1': 'test_password',
            'password2': 'test_pass'
        }

        return super().setUp()
    
class RegisterTest(BaseTest):
    def test_can_view_signup_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_cannot_register_user_short_password(self):
        response = self.client.post(self.register_url, self.user_short_password, format='text/html')
        self.assertEqual(response.status_code, 400)

    def test_cannot_register_user_similar_to_username(self):
        response = self.client.post(self.register_url, self.user_similar_username, format='text/html')
        self.assertEqual(response.status_code, 400)

    def test_cannot_register_user_only_numbers(self):
        response = self.client.post(self.register_url, self.user_only_numbers, format='text/html')
        self.assertEqual(response.status_code, 400)

    def test_cannot_register_user_not_matching_passwords(self):
        response = self.client.post(self.register_url, self.user_not_matching_passwords, format='text/html')
        self.assertEqual(response.status_code, 400)

    def test_can_view_sign_up_sucess_page_correctly(self):
        response = self.client.get(self.sign_up_page_success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign_up_success.html')

class LoginTest(BaseTest):
    def test_can_view_profile_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
    
class ProfileTest(BaseTest):
    def test_can_view_profile_page_correctly(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.login(username='test_username_pass', password='password.123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

class UserUpdateTest(BaseTest):
    def test_can_view_update_user_page_correctly(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.login(username='test_username_pass', password='password.123')
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/update_user.html')

    def test_can_update_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.login(username='test_username_pass', password='password.123')
        response = self.client.post(self.update_url, self.user_update, format='text/html')
        self.assertEqual(response.status_code, 302)