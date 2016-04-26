import sys, os

sys.path.insert(0, os.path.split(os.path.abspath(__file__))[0])

from lassgdk import app as application
from lassgdk import config

class Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = config.environ
        return self.app(environ, start_response)

application.wsgi_app = Middleware(application.wsgi_app)

if __name__ == "__main__":
    app.run(debug=True)
