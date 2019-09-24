import unittest

from app import app

class Tests(unittest.TestCase):

    @classmethod
    def startUpClass(cls):
        pass 

    @classmethod
    def takeDownClass(cls):
        pass 

    # startup and takedown
    def startUp(self):
        pass

    def takeDown(self):
        pass

    # Tests

    def test_get_routes(self):
        tester = app.test_client(self)
    # Homepage
        response = tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # Get Recipes
        response = tester.get('/get_recipes', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # Add Recipes
        response = tester.get('/add_recipes', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # Data
        response = tester.get('/data', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # Signup
        response = tester.get('/signup', content_type="html/text")
        self.assertEqual(response.status_code, 200)
    # Login
        response = tester.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200)
  
        
    def test_get_routes_connect_template(self):
        tester = app.test_client(self)
     # Homepage
        response = tester.get('/', content_type="html/text")
        self.assertTrue(b'Get fit with Fitness Cookbook' in response.data)
    # Get Recipes
        response = tester.get('/get_recipes', content_type="html/text")
        self.assertTrue(b'Recipes' in response.data)
    # Add Recipes
        response = tester.get('/add_recipes', content_type="html/text")
        self.assertTrue(b'Recipes' in response.data)
    # Data
        response = tester.get('/data', content_type="html/text")
        self.assertTrue(b'Data Overview' in response.data)
    # Signup
        response = tester.get('/signup', content_type="html/text")
        self.assertTrue(b'Please Signup' in response.data)    
    # Login
        response = tester.get('/login', content_type="html/text")
        self.assertTrue(b'Please Login' in response.data)
    
if __name__ == "__main__":
    unittest.main()