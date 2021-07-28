##Patnox 27-07-2021

from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework.exceptions import ValidationError, ParseError
from django.test import TestCase, Client
from django.urls import reverse
from checkpoints.models import CheckedPoints
from checkpoints.serializers import CheckedPointsSerializer
import json

# initialize the APIClient app
# client = Client()
client = APIClient()

class CheckPointsTest(APITestCase):
    """ Test module for checking nearest points """
    
    def setUp(self):
        self.valid_payload_01 = {
            "data": {
                "type": "CheckedPoints",
                "attributes": {
                    "query": "[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]"
                }
            }
        }
        self.valid_payload_02 = {
            "data": {
                "type": "CheckedPoints",
                "attributes": {
                    "query": "[(-9,10),(11,-34),(-15,33),(44,21),(43,13),(38,5),(-11,39),(-35,9),(46,43),(-49,-32)]"
                }
            }
        }
        self.valid_payload_03 = {
            "data": {
                "type": "CheckedPoints",
                "attributes": {
                    "query": "[(-31,10),(19,-46),(28,-6),(-11,4),(-48,-15),(50,34),(-11,-7),(31,13),(16,30),(-50,-17)]"
                }
            }
        }
        self.invalid_payload_01 = {
            "data": {
                "type": "CheckedPoints",
                "attributes": {
                    "query": ""
                }
            }
        }
        self.invalid_payload_02 = {
            "data": {
                "type": "CheckedPoints",
                "attributes": {
                    "query": "[(2,a),(2,2)]"
                }
            }
        }
        self.invalid_payload_03 = {
            "data": {
                "type": "CheckedPoints",
                "attributes": {
                    "query": "CDC0DCB256CC26A7092BB0D06C3E5AF85AE1BEF52D05199913F286D5F01DEAD1"
                }
            }
        }

    def test_create_valid_pointcheck(self):
        response = self.client.post('/checkpoints/', self.valid_payload_01, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('response'), '((1, 1), (-1, -1))')
        response = self.client.post('/checkpoints/', self.valid_payload_02, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('response'), '((-15, 33), (-11, 39))')
        response = self.client.post('/checkpoints/', self.valid_payload_03, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('response'), '((-48, -15), (-50, -17))')

    def test_create_invalid_pointcheck(self):
        response = self.client.post('/checkpoints/', self.invalid_payload_01, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.post('/checkpoints/', self.invalid_payload_02, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.post('/checkpoints/', self.invalid_payload_03, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

