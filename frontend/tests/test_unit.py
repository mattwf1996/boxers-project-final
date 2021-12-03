from application import app
from application.routes import backend_host_host
from flask import url_for
from flask_testing import TestCase
import requests_mock

test_data = {
    "id": 1,
    "name": "Test Division 1",
    "weight_range": 150-250,
    "boxers": [
        {
            "id": 1,
            "weight": 200,
            "name": "Test Boxer",
            "division_id": 1
        }
    ]
}

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):

    def test_home_get(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/get/allDivisions", json={'divisions': []})
            response = self.client.get(url_for('home'))
            self.assert200(response)

    def test_home_create_division(self):
        response = self.client.get(url_for('create_division'))
        self.assert200(response)

class TestHome(TestBase):

    def test_home_read_divisions(self):
        with requests_mock.Mocker() as m:
            m.get(f"http://{backend_host}/get/allDivisions", json={'divisions': [test_data]})
            response = self.client.get(url_for('home'))
            self.assertIn("Test Division 1", response.data.decode("utf-8"))
    
class TestCreateDivision(TestBase):

    def test_create_division_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/create/division", text="Test response")
            m.get(f"http://{backend_host}/get/allDivisions", json={'divisions': [test_data]})
            response = self.client.post(url_for('create_division'), follow_redirects=True)
            self.assertIn("Test Division 1", response.data.decode("utf-8"))

class TestCreateBoxer(TestBase):

    def test_create_boxer_form_post(self):
        with requests_mock.Mocker() as m:
            m.post(f"http://{backend_host}/create/boxer/1", text="Test response")
            m.get(f"http://{backend_host}/get/allDivisions", json={'divisions': [test_data]})
            response = self.client.post(url_for('create_division'), follow_redirects=True)
            self.assertIn("Test Division 1", response.data.decode("utf-8"))