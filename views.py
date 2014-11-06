from cgi import escape

def index(environ, start_response):
    """This function will be mounted on "/" and display a link to the hello world page."""
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello World Application 
    
            This is the Hello World application:

            `continue <hello/>`_

            ''']

def hello(environ, start_response):
    """Like the example above, but it uses the name specified in the URL."""
    # get the name from the url if it was specified there.
    args = environ['i_think_i_can_call_this_kirby.args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
            Hello %(subject)s!

            ''' % {'subject': subject}]

def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']

