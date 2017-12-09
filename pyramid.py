from pyramid.config import Configurator
from pyramid.response import Response
from wsgiref.simple_server import make_server
from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

assets = [
  'app.js',
  'react.js',
  'leaflet.js',
  'D3.js',
  'moment.js',
  'math.js',
  'main.css',
  'bootstrap.css',
  'normalize.css',
  ]
  
styles = []
scripts = []

for str in assets
    b = str.split('.')
    if b[1] == "js":
        scripts.append(str)
    else:
        styles.append(str)


class WsgiTopBottomMiddleware(object):
    def _init_(self, app):
        self.app = app
    
     def __call__(self, environ, start_response):
        response = self.app(environ, start_response).decode() 
        if response.find('<body>') > -1:
            head1, head = response.split('<head>')
            datahead, endhead = head.split('</head>')
            head2, body = endhead.split('<body>')
            databody, endbody = body.split('</body>')

            yield (head1 + data + endbody).encode()  
        else:
            yield (response).encode()

def index (request):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')
    print(template.render(js=scripts, css=styles))

def aboutme (request):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('/about/aboutme.html')
    print(template.render(js=scripts, css=styles))

if __name__ == '__main__':
    configuration = Configurator()
    configuration.add_route('aboutme', '/aboutme/aboutme.html')
    configuration.add_view(aboutme, route_name='aboutme')
    configuration.add_route('index', '/index.html')
    configuration.add_view(index, route_name='index')
    app = configuration.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
