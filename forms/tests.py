# forms/tests.py
from django.test import TestCase
from django.urls import reverse
from forms.models import Form

class FormMatcherTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Создание тестовых шаблонов форм"""
        Form.objects.create(
            name="User Registration",
            fields={
                "email": "email",
                "phone": "phone",
                "birth_date": "date"
            }
        )
        Form.objects.create(
            name="Order Form",
            fields={
                "user_email": "email",
                "order_date": "date",
                "customer_phone": "phone"
            }
        )

    def test_matching_template(self):
        """Тест на успешное нахождение подходящего шаблона"""
        url = reverse('get_form')
        data = {
            "fields": {
                "email": "test@example.com",
                "phone": "+7 123 456 78 90",
                "birth_date": "1990-12-31"
            }
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"form_name": "User Registration"})

    def test_no_matching_template(self):
        """Тест на отсутствие подходящего шаблона"""
        url = reverse('get_form')
        data = {
            "fields": {
                "unknown_field": "test@example.com",
                "phone": "+7 123 456 78 90"
            }
        }
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "unknown_field": "email",
            "phone": "phone"
        })

    def test_invalid_input(self):
        """Тест на неправильный формат входных данных"""
        url = reverse('get_form')
        data = {"invalid_key": "value"}
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
