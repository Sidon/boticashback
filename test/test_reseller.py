from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from django.urls import reverse

from apps.reseller.models import Reseller


class ResellerAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.Reseller = Reseller.objects.create_reseller(
            'admin_reseler@test.net',
            'Testing Reseller Login',
            '21734085002',
            'master123'
        )
        cls.password = 'master123'

    def test_create_Reseller(self):
        url = reverse('reseller:resellers-list')
        data = {
            "email": "Reseller@test.net",
            "full_name": "Testing Reseller",
            "cpf": "90044044062",
            "password": "master123",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def login_jwt(self):
        url = reverse('token_obtain_pair')
        data = {
            'email': self.Reseller.email,
            'password': self.password
        }
        return self.client.post(url, data=data)

    def test_login(self):
        response = self.login_jwt()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data['access'], response.data['refresh'])
        self.access = response.data['access']
        self.refresh = response.data['refresh']

    def test_create_unique_email(self):
        url = reverse('reseller:resellers-list')
        data = {
            "email": "admin_reseler@test.net",
            "name": "Creating unique Reseller via test",
            "cpf": "00707566860",
            "password": "master123",
        }
        response = self.client.post(url, data)
        for error in response.data['email']:
            self.assertEqual(error.code, 'unique')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_cpf(self):
        url = reverse('reseller:resellers-list')
        data = {
            "email": "unique_cpf@test.net",
            "name": "Testing Reseller cpf",
            "cpf": "00707566866",
            "password": "master123",
        }
        response = self.client.post(url, data)
        print(dir(response))
        for error in response.data['cpf']:
            self.assertEqual(error.code, 'invalid')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReselerTestCase(TestCase):

    def test_create_reseler(self):
        """ Testing the creation of a reseller """
        reseller = Reseller.objects.create_reseller(
            'reseller@test.net',
            'Reseler Testing via Testcase',
            '21734085002',
            'master123'
        )
        self.assertEqual(reseller.email, 'reseller@test.net')
        self.assertEqual(reseller.full_name, 'Reseler Testing via Testcase')
        self.assertEqual(reseller.cpf, '21734085002')
