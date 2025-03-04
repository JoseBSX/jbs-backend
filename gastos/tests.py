from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Gasto
from rest_framework.test import APIClient


class GastoAPITestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='my_user', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.gasto = Gasto.objects.create(
            usuario=self.user,
            categoria='entretenimiento',
            monto=56.67
        )
        self.gasto_url = f'/api/gastos/{self.gasto.id}/'

    def test_create_gasto(self):
        data = {
            'usuario': 'my_user',
            'categoria': 'transporte',
            'monto': 100.50
        }
        response = self.client.post('/api/gastos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_gasto_list(self):
        response = self.client.get('/api/gastos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_gasto_detail(self):
        response = self.client.get(self.gasto_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['categoria'], 'entretenimiento')

    def test_update_gasto(self):
        data = {
            'usuario': 'my_user',
            'categoria': 'comida',
            'monto': 75.00
        }
        response = self.client.put(self.gasto_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.gasto.refresh_from_db()
        self.assertEqual(self.gasto.monto, 75.00)

    def test_delete_gatso(self):
        response = self.client.delete(self.gasto_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Gasto.objects.filter(id=self.gasto.id).exists())
