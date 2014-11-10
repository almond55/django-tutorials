import sys
import re
import views
import settings
import importlib

root_urlconf = settings.ROOT_URLCONF
try:
    root_urlconf_module = importlib.import_module(root_urlconf)
except (ImportError):
    print 'Module path in settings.py is incorrect. Please check your module path'  
    sys.exit()

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to
    the functions from above and store the regular expression
    captures in the WSGI environment as  `myapp.url_args` so that
    the functions from above can access the url placeholders.

    If nothing matches call the `not_found` function.
    """
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in root_urlconf_module.urlpatterns:
        match = re.search(regex, path)
        if match is not None:
            environ['i_think_i_can_call_this_kirby.args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
