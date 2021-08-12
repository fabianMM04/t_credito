import json
from django.test import TestCase
from http import HTTPStatus

from .models import Franquicia
# Create your tests here.


class FranquiciaTest(TestCase):
    fixtures = ['franquicias.json']

    def test_fixture(self):
        self.assertEqual(len(Franquicia.objects.all()), 4)

    def test_submission_without_content_type(self):
        response = self.client.post('/api/v1/franquicia', data={})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(len(Franquicia.objects.all()), 4)

    def test_valid_submission(self):
        response = self.client.post('/api/v1/franquicia', data={'nombre': 'prueba', 'cantidad_numero': 12, 'numero_inicial': 1}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Franquicia.objects.all()), 5)

    def test_incomplete_submission(self):
        response = self.client.post('/api/v1/franquicia', data={'cantidad_numero': 12, 'numero_inicial': 1}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(Franquicia.objects.all()), 4)
       
    def test_get_all_franquicias(self):
        response = self.client.get('/api/v1/franquicia')
        self.assertEqual(response.status_code, 200)
        actual_value = response.json()['franquicias']
        self.assertEqual(len(actual_value), 4)

    def test_not_found_get_franquicia(self):
        response = self.client.get('/api/v1/franquicia/0')
        self.assertEqual(response.status_code, 404)
        
    def test_found_franquicia(self):
        response = self.client.get('/api/v1/franquicia/1')
        self.assertEqual(response.status_code, 200)
        actual_value = response.json()['franquicia']
        expected = {   "id": 1, "nombre": "Visa", "cantidad_numero": 16, "numero_inicial": 4}
        self.assertEqual(actual_value, expected)

    def test_not_found_put_franquicia(self):
        response = self.client.put('/api/v1/franquicia/0')
        self.assertEqual(response.status_code, 404)

    def test_update_franquicia_without_contenttype(self):
        response = self.client.put('/api/v1/franquicia/1', data={'nombre': 'PRUEBA', 'cantidad_numero': 118})
        self.assertEqual(response.status_code, 500)

    def test_update_franquicia_with_contenttype(self):
        response = self.client.put('/api/v1/franquicia/1', data={'nombre': 'PRUEBA', 'cantidad_numero': 118}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        expected = {'nombre': 'PRUEBA', 'cantidad_numero': 118}
        actual_value = Franquicia.objects.get(pk=1)
        self.assertEqual(actual_value.nombre, expected['nombre'])
        self.assertEqual(actual_value.cantidad_numero, expected['cantidad_numero'])

    def test_not_found_delete_franquicia(self):
        response = self.client.delete('/api/v1/franquicia/0')
        self.assertEqual(response.status_code, 404)    

    def test_delete_franquicia(self):
        response = self.client.delete('/api/v1/franquicia/1')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Franquicia.objects.all()), 3) 

    