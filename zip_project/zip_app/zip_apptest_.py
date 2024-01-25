# test_views.py
from django.test import TestCase, RequestFactory
from . import views
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zip_project.settings')
settings.configure()

class DistanceCalculatorTestCase(TestCase):
    def setUp(self):
        # create a RequestFactory instance
        self.factory = RequestFactory()

    def test_valid_zipcodes(self):
        # create a mock GET request with valid zipcodes
        request = self.factory.get('/distance_calculator?zip1=10001&zip2=90210')
        # call the distance_calculator view function with the request
        response = views.distance_calculator(request)
        # assert that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # assert that the result in the context matches the expected distance
        self.assertEqual(response.context_data['result'], 'The Distance between 10001 and 90210 is 2448.16 miles.')

    def test_invalid_zipcodes(self):
        # create a mock GET request with invalid zipcodes
        request = self.factory.get('/distance_calculator?zip1=abcde&zip2=12345')
        # call the distance_calculator view function with the request
        response = views.distance_calculator(request)
        # assert that the response status code is 302, indicating a redirect
        self.assertEqual(response.status_code, 302)
        # assert that the response redirects to the index page
        self.assertEqual(response.url, '/')
        # assert that the response shows an error message
        self.assertEqual(response.cookies['messages'].value, 'Invalid input. Please enter a 5 digit US Zipcode. Program will not accept letters or special characters.')
