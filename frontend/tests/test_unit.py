from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

class TestViews(TestBase):
    # Test whether we get a successful response from our routes
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
    
    def test_create_boxer_get(self):
        response = self.client.get(url_for('create_boxer'))
        self.assert200(response)

    def test_read_boxers_get(self):
        response = self.client.get(url_for('read_boxers'))
        self.assert200(response)

    def test_update_boxer_get(self):
        response = self.client.get(url_for('update_boxer', id=1))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_boxers(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)
    
class TestCreate(TestBase):

    def test_create_boxer(self):
        response = self.client.post(
            url_for('create_boxer'),
            data={"description": "Testing create functionality"},
            follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)
    
# class TestUpdate(TestBase):

#     def test_update_boxer(self):
#         response = self.client.post(
#             url_for('update_boxer', id=1),
#             data={"description": "Testing update functionality"},
#             follow_redirects=True
#         )
#         self.assertIn(b"Testing update functionality", response.data)
    
    # def test_complete_boxer(self):
    #     response = self.client.get(url_for('complete_boxer', id=1), follow_redirects=True)
    #     self.assertEqual(False, True)
    
    # def test_incomplete_boxer(self):
    #     response = self.client.get(url_for('incomplete_boxer', id=1), follow_redirects=True)
    #     self.assertEqual(Boxers.query.get(1).completed, False)
        

# class TestDelete(TestBase):

#     def test_delete_boxer(self):
#         response = self.client.get(
#             url_for('delete_boxer', id=1),
#             follow_redirects=True
#         )
#         self.assertNotIn(b"Run unit tests", response.data)
