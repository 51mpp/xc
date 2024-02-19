import unittest
from app import restapi

class TestRestAPI(unittest.TestCase):
    def setUp(self):
        self.app = restapi.app.test_client()

    def test_plus_int(self):
        response = self.app.get('/plus/1/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 3})
        
    def test_plus_zero(self):
        response = self.app.get('/plus/0/0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 0})
        
    def test_plus_negative(self):
        response = self.app.get('/plus/-1/-2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': -3})
        
    def test_plus_int_float(self):
        response = self.app.get('/plus/1/2.5')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Invalid input'})
        
    def test_plus_float(self):
        response = self.app.get('/plus/1.5/2.5')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Invalid input'})
        
    def test_plus_string(self):
        response = self.app.get('/plus/1/abc')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Invalid input'})
        
    def test_plus_string_string(self):
        response = self.app.get('/plus/abc/def')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Invalid input'})
    
if __name__ == '__main__':
    unittest.main()