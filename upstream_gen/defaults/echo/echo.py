"""
Upstream server used for testing how a load balancer changes affects request
"""
# coding: utf-8
import logging
import sys
from flask import Flask
from flask import redirect
from flask import jsonify
from flask import request
from flask.views import MethodView

from flasgger import Swagger
from upstream_gen.defaults.echo.config import SWAGGER_CONFIG

LOGGER = logging.getLogger(__name__)
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: LOGGER.debug(x)

app = Flask(__name__)
app.config['SWAGGER'] = SWAGGER_CONFIG
# making sure json reply is pretty printed
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.logger = LOGGER
swag = Swagger(app)
# https://stackoverflow.com/questions/15974730/how-do-i-get-the-different-parts-of-a-flask-requests-url

# => curl -XGET http://127.0.0.1:5000/alert/dingding/test?x=y

#request.method:              GET
# request.url:                 http://127.0.0.1:5000/alert/dingding/test?x=y
# request.base_url:            http://127.0.0.1:5000/alert/dingding/test
#request.url_charset:         utf-8
# request.url_root:            http://127.0.0.1:5000/
# str(request.url_rule):       /alert/dingding/test
# request.host_url:            http://127.0.0.1:5000/
# request.host:                127.0.0.1:5000
# request.script_root:
# request.path:                /alert/dingding/test
# request.full_path:           /alert/dingding/test?x=y
# request.args:                ImmutableMultiDict([('x', 'y')])
# request.args.get('x'):       y


class BaseAPIView(MethodView):
    """BAse view"""


class ModelAPIView(BaseAPIView):
    """Model api view"""



class echoView(ModelAPIView):
    responses = {
        200: {
            'description': 'Request was successful',
        }
    }
    tags = ['echo']
    consumes = ['application/json']
    produces = ['application/json']
    schemes = ['http', 'https']
    deprecated = False
    summary = "Post request demo"
    description = "Testing server responce to post request behind load balancer"

    def post(self, endpoint):
        """
        it just returns back the payload as json
        ---
        tags:
          - echo
        parameters:
          - name: endpoint
            in: path
            description: some sample endpoint
            required: true
        definitions:
          Request:
            type: object
            properties:
              path:
                type: string
              method:
                type: string
              headers:
                type: object
              params:
                type: object
              body:
                type: string
        responses:
          200:
            description: echos back the request
        """
        result = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args,
            'body': request.data.decode("utf-8")
        }
        return jsonify(result)

    def get(self, endpoint):
        """
        it just returns back the payload as json
				---
        tags:
          - echo
        parameters:
          - name: endpoint
            in: path
            description: some sample endpoint
            required: true
        definitions:
          Request:
            type: object
            properties:
              path:
                type: string
              method:
                type: string
              headers:
                type: object
              params:
                type: object
              body:
                type: string
        responses:
          200:
            description: echos back the request
        """
        result = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args,
            'body': request.data.decode("utf-8")

        }
        return jsonify(result)

    def put(self, endpoint):
        """
        it just returns back the payload as json
				---
        tags:
          - echo
        parameters:
          - name: endpoint
            in: path
            description: some sample endpoint
            required: true
        definitions:
          Request:
            type: object
            properties:
              path:
                type: string
              method:
                type: string
              headers:
                type: object
              params:
                type: object
              body:
                type: string
        responses:
          200:
            description: echos back the request
        """
        result = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args,
            'body': request.data.decode("utf-8")

        }
        return jsonify(result)

    def head(self, endpoint):
        """
        it just returns back the payload as json
				---
        tags:
          - echo
        parameters:
          - name: endpoint
            in: path
            description: some sample endpoint
            required: true
        definitions:
          Request:
            type: object
            properties:
              path:
                type: string
              method:
                type: string
              headers:
                type: object
              params:
                type: object
              body:
                type: string
        responses:
          200:
            description: echos back the request
        """
        result = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args,
            'body': request.data.decode("utf-8")

        }
        return jsonify(result)

    def delete(self, endpoint):
        """
        it just returns back the payload as json
				---
        tags:
          - echo
        parameters:
          - name: endpoint
            in: path
            description: some sample endpoint
            required: true
        definitions:
          Request:
            type: object
            properties:
              path:
                type: string
              method:
                type: string
              headers:
                type: object
              params:
                type: object
              body:
                type: string
        responses:
          200:
            description: echos back the request
        """
        result = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args,
            'body': request.data.decode("utf-8")

        }
        return jsonify(result)

    def patch(self, endpoint):
        """
        it just returns back the payload as json
				---
        tags:
          - echo
        parameters:
          - name: endpoint
            in: path
            description: some sample endpoint
            required: true
        definitions:
          Request:
            type: object
            properties:
              path:
                type: string
              method:
                type: string
              headers:
                type: object
              params:
                type: object
              body:
                type: string
        responses:
          200:
            description: echos back the request
        """
        result = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args,
            'body': request.data.decode("utf-8")

        }
        return jsonify(result)

    def options(self, endpoint):
        """
        it just returns back the payload as json
				---
        tags:
          - echo
        parameters:
          - name: endpoint
            in: path
            description: some sample endpoint
            required: true
        definitions:
          Request:
            type: object
            properties:
              path:
                type: string
              method:
                type: string
              headers:
                type: object
              params:
                type: object
              body:
                type: string
        responses:
          200:
            description: echos back the request
        """
        result = {
            'path': request.path,
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args,
            'body': request.data.decode("utf-8")
        }
        return jsonify(result)

app.add_url_rule(
    '/<path:endpoint>',
    view_func=echoView.as_view('echo'),
    methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS']
)


@app.route("/")
def index():
    return redirect("/echo/apidocs")


if __name__ == "__main__":
    app.run(debug=True)
