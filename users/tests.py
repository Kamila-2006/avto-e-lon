from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UsersAPITestCase(APITestCase):
    def setUp(self):
        self.registration_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'user_type': 'regular',
            'password': 'testpassword123',
            'password_confirm': 'testpassword123'
        }
        response = self.client.post(reverse('user-register'), self.registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.user_id = response.data['id']
        self.token = response.data['token']

    def test_user_login(self):
        url = reverse('user-login')
        data = {
            'username': self.registration_data['username'],
            'password': self.registration_data['password']
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_profile(self):
        url = reverse('user-profile', kwargs={'pk': self.user_id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user_id)
        self.assertEqual(response.data['username'], self.registration_data['username'])
        self.assertEqual(response.data['email'], self.registration_data['email'])
