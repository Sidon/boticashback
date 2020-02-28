from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import  APIClient
from django.test import TestCase
from apps.reseller.models import Reseller

User = get_user_model()

class TestApiDrf(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.password = 'master123'
        cls.reseller = Reseller.objects.create_reseller(
            'reseler_test@test.net',
            'Testing Reseller Login',
            '21734085002',
            cls.password,
        )
        cls.client = APIClient()

        # Obter os tokens
        url = reverse('token_obtain_pair')
        data = {
           'email': cls.reseller.email,
           'password': cls.password
        }
        response = cls.client.post(url, data=data)
        cls.tokens = response.data

    # Obter os endpoints na raiz da versão da api
    def test_get_root_endpoint(self):
        url = reverse('api-root:api-root')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Cadastrar um revendedor
    def test_create_Reseller(self):
        url = reverse('api-root:reselers-list')
        data = {
            "email": 'frank@zappa.net',
            "full_name": 'Frank Vincent Zappa',
            "cpf": "62824448709",
            "password": "master123",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Cadastrar um CPF pré aprovado
    def test_cadastro_cpf(self):
        url = reverse('api-root:cpfs-list')
        data = {
            "cpf": "33242253701",
            "description": "CPF pre aprovado 1"
        }
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Cadastrar uma compra de outro venddor
    def test_cadastrar_compra_outro(self):
        url = reverse('api-root:admin-compras-list')
        data = {
            "reseller": 1,
            "date_purchase": "2020-02-28",
            "code": "1234",
            "purchase_value": 540.00
        }

        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Cadastrar uma compra do vendedor logado
    def test_cadastrar_compra_logado(self):
        url = reverse('api-root:compras-list')
        data = {
            "date_purchase": "2020-02-28",
            "code": "1234",
            "purchase_value": 540.00
        }

        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Obter lista de cpfs pré cadastrados
    def test_get_cpfs(self):
        url = reverse('api-root:cpfs-list')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Obter lista de cashback na aplicação
    def test_get_casback_list(self):
        url = reverse('api-root:cashback-lista-list')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Obter cashback acumulado via endpoint fornecido
    def test_get_casback_endpoint(self):
        url = reverse('api-root:cashback-acumulado-list')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
