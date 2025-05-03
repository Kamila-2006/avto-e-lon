from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from cars.models import Make, Model, BodyType, Feature, Car

User = get_user_model()

class CarAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.make = Make.objects.create(name='Toyota', country='Japan')
        self.model = Model.objects.create(name='Camry', make=self.make)
        self.body_type = BodyType.objects.create(name='Sedan')
        self.feature1 = Feature.objects.create(name='ABS', category='Safety')
        self.feature2 = Feature.objects.create(name='Airbag', category='Safety')

        self.car_data = {
            'make': self.make.id,
            'model': self.model.id,
            'year': 2020,
            'body_type': self.body_type.id,
            'fuel_type': 'petrol',
            'transmission': 'automatic',
            'color': 'White',
            'mileage': 45000,
            'engine_size': 2.0,
            'power': 180,
            'drive_type': 'front',
            'features': [self.feature1.id, self.feature2.id],
            'vin': 'TESTVIN123456789'
        }

    def test_list_cars_anonymous(self):
        self.client.logout()
        response = self.client.get('/api/cars/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_car_authenticated(self):
        response = self.client.post('/api/cars/', self.car_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['make']['name'], 'Toyota')

    def test_get_car_detail(self):
        create_response = self.client.post('/api/cars/', self.car_data, format='json')
        car_id = create_response.data['id']
        self.client.logout()
        response = self.client.get(f'/api/cars/{car_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_car(self):
        create_response = self.client.post('/api/cars/', self.car_data, format='json')
        car_id = create_response.data['id']
        updated_data = self.car_data.copy()
        updated_data['color'] = 'Black'
        response = self.client.put(f'/api/cars/{car_id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['color'], 'Black')

    def test_delete_car(self):
        create_response = self.client.post('/api/cars/', self.car_data, format='json')
        car_id = create_response.data['id']
        response = self.client.delete(f'/api/cars/{car_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
