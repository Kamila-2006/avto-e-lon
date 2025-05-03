from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from users.models import Dealer


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

class DealerAPITestCase(APITestCase):
    def setUp(self):
        self.registration_data = {
            'username': 'dealeruser',
            'email': 'dealer@example.com',
            'first_name': 'Dealer',
            'last_name': 'User',
            'user_type': 'dealer',
            'password': 'testpassword123',
            'password_confirm': 'testpassword123'
        }
        response = self.client.post(reverse('user-register'), self.registration_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.token = response.data['token']
        self.user_id = response.data['id']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.dealer_data = {
            "company_name": "Test Auto",
            "description": "Test description",
            "website": "https://testauto.uz",
            "address": "Tashkent"
        }
        create_url = reverse('dealers-list')
        response = self.client.post(create_url, self.dealer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.dealer_id = response.data['id']

        self.client.credentials()  # сброс токена

    def test_list_dealers_anonymous(self):
        url = reverse('dealers-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dealer_detail_anonymous(self):
        url = reverse('dealers-detail', args=[self.dealer_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_dealer_unauthenticated(self):
        url = reverse('dealers-list')
        response = self.client.post(url, self.dealer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_dealer_owner(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('dealers-detail', args=[self.dealer_id])
        updated_data = {
            "company_name": "Updated Auto",
            "description": "Updated description",
            "website": "https://updatedauto.uz",
            "address": "New Tashkent"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company_name'], "Updated Auto")

    def test_delete_dealer_owner(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = reverse('dealers-detail', args=[self.dealer_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)