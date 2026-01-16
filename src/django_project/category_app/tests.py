from django.test import TestCase
from rest_framework.test import APITestCase


class TestCategoryAPI(APITestCase):
    def test_ist_categories(self):
        url = "/api/categories/"
        response = self.client.get(url)

        expected_data = [
            {
                "id": "9bc488a6f47ca-450c-9c59-033447112676",
                "name": "Movie",
                "description": "Movie description",
                "is_active": True
            },
            {
                "id": "6f7c2133-f1d3-4040-b700-c547453345d3",
                "name": "Documentary",
                "description": "Documentary description",
                "is_active": True
            }
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
