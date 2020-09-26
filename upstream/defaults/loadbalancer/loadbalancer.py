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
from flasgger import Swagger
from flasgger import SwaggerView
from upstream.defaults.loadbalancer.config import SWAGGER_CONFIG

LOGGER = logging.getLogger(__name__)
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: LOGGER.debug(x)

app = Flask(__name__)
app.config['SWAGGER'] = SWAGGER_CONFIG
app.logger = LOGGER
swag = Swagger(app)


class LoadBalancerView(SwaggerView):
    responses = {
        200: {
            'description': 'Request was successful',
        }
    }
    tags = ['loadbalancer']
    consumes = ['application/json']
    produces = ['application/json']
    schemes = ['http', 'https']
    deprecated = False
    summary = "Post request demo"
    description = "Testing server responce to post request behind load balancer"

    def post(self):
        """
        it just returns back the payload as json
        """
        result = {
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        return jsonify(result)

    def get(self):
        """
        it just returns back the payload as json
        """
        result = {
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        return jsonify(result)

    def put(self):
        """
        it just returns back the payload as json
        """
        result = {
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        return jsonify(result)

    def head(self):
        """
        it just returns back the payload as json
        """
        result = {
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        return jsonify(result)

    def delete(self):
        """
        it just returns back the payload as json
        """
        result = {
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        return jsonify(result)

    def patch(self):
        """
        it just returns back the payload as json
        """
        result = {
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        return jsonify(result)

    def options(self):
        """
        it just returns back the payload as json
        """
        result = {
            'method': request.method,
            'headers': dict(request.headers),
            'params': request.args
        }
        return jsonify(result)


app.add_url_rule(
    '/trigger',
    view_func=LoadBalancerView.as_view('loadbalancer'),
    methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS']
)


@app.route("/")
def index():
    return redirect("/loadbalancer/apidocs")


if __name__ == "__main__":
    app.run(debug=True)
