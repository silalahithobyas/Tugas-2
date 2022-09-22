from django.test import TestCase, Client

# Create your tests here.
class TestUrl(TestCase):
    def test_html_url(self):
        client = Client()
        response = client.get('http://localhost:8000/mywatchlist/html/')
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        client = Client()
        response = client.get('http://localhost:8000/mywatchlist/json/')
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        client = Client()
        response = client.get('http://localhost:8000/mywatchlist/xml/')
        self.assertEquals(response.status_code, 200)