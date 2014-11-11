import unittest

from main import application, next_application

def start_response(*args, **kwargs):
    pass

class TestApplication(unittest.TestCase):
    def test_root_path(self):
        environ = {
            'PATH_INFO': '/', 
        }

        response = application(environ, start_response)
        self.assertTrue('Hello World Application ' in "".join(response))

    def test_hello_aman(self):
        environ = {
            'PATH_INFO': '/hello/aman', 
        }

        response = application(environ, start_response)
        self.assertTrue('Hello aman' in "".join(response))

class TestNextApplication(unittest.TestCase):
    def test_first(self):
        out = next_application('1', '2', '3')
        self.assertEqual(out, ['1', '2', '3'])

if __name__ == '__main__':
    unittest.main()
