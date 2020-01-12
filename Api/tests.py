from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.core.management import call_command
from .models import Company, People


#  Import data
def setUpModule():
    call_command('data2db')
  

class TestAPI(TestCase):
    def setUp(self):
        client = Client(SERVER_NAME='localhost')

    def test_get_existing_company(self):
        result = self.client.get('/v1/api/employees/1/')
        self.assertEqual(result.status_code, 200)

    def test_get_not_existing_company(self):
        result = self.client.get('/v1/api/employees/not_existing_company/')
        self.assertEqual(result.status_code, 404)

    def test_get_samefriends(self):
        result = self.client.get('/v1/api/samefriends/1/2/')
        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(result.json()["people1"])
        self.assertIsNotNone(result.json()["people2"])
        self.assertIsNotNone(result.json()["same_friends"])

    def test_get_no_samefirends(self):
        result = self.client.get('/v1/api/samefriends/1/212312/')
        self.assertEqual(result.status_code, 404)
    
    def test_get_food(self):
        result = self.client.get('/v1/api/fruit_and_vegetable/1/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json()["fruits"])
        self.assertTrue(result.json()["vegatables"])
        

