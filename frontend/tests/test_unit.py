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


# from flask import url_for
# from flask_testing import TestCase
# from application import app

# class TestBase(TestCase):

#     def create_app(self):
#         # Defines the flask object's configuration for the unit tests
#         app.config.update(
#             DEBUG=True,
#             WTF_CSRF_ENABLED=False
#         )
#         return app

# class TestViews(TestBase):
#     # Test whether we get a successful response from our routes
#     def test_home_get(self):
#         response = self.client.get(url_for('home'))
#         self.assert200(response)
    
#     def test_create_boxer_get(self):
#         response = self.client.get(url_for('create_boxer'))
#         self.assert200(response)

#     def test_read_boxers_get(self):
#         response = self.client.get(url_for('read_boxers'))
#         self.assert200(response)

#     def test_update_boxer_get(self):
#         response = self.client.get(url_for('update_boxer', id=1))
#         self.assert200(response)

# class TestRead(TestBase):

#     def test_read_home_boxers(self):
#         response = self.client.get(url_for('home'))
#         self.assertIn(b"Run unit tests", response.data)
    
# class TestCreate(TestBase):

#     def test_create_boxer(self):
#         response = self.client.post(
#             url_for('create_boxer'),
#             data={"description": "Testing create functionality"},
#             follow_redirects=True
#         )
#         self.assertIn(b"Testing create functionality", response.data)
    
# class TestUpdate(TestBase):

#     def test_update_boxer(self):
#         response = self.client.post(
#             url_for('update_boxer', id=1),
#             data={"description": "Testing update functionality"},
#             follow_redirects=True
#         )
#         self.assertIn(b"Testing update functionality", response.data)
    
#     def test_complete_boxer(self):
#         response = self.client.get(url_for('complete_boxer', id=1), follow_redirects=True)
#         self.assertEqual(False, True)
    
#     def test_incomplete_boxer(self):
#         response = self.client.get(url_for('incomplete_boxer', id=1), follow_redirects=True)
#         self.assertEqual(Boxers.query.get(1).completed, False)
        

# class TestDelete(TestBase):

#     def test_delete_boxer(self):
#         response = self.client.get(
#             url_for('delete_boxer', id=1),
#             follow_redirects=True
#         )
#         self.assertNotIn(b"Run unit tests", response.data)
