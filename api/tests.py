from rest_framework.test import APITestCase


class HealthTests(APITestCase):
    def test_health_returns_200(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)

    def test_health_status_ok(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.json()["status"], "ok")

    def test_health_includes_version(self):
           response = self.client.get("/api/health/")
           self.assertEqual(response.json()["version"], "1.0")