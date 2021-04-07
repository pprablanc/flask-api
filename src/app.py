"""Flask Application"""

# flask/flask_restful libraries

# TODO: test connexion compatilibility with other libraries
#from flask import render_template, jsonify
#import connexion
from flask import Flask, jsonify, render_template
from flask_restful import Api

# apispec libraries and plugins
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
#from apispec_webframeworks.flask import FlaskPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec import marshal_with, doc, use_kwargs

# library for data formating (object serialization)
from marshmallow import Schema, fields

# endpoints classes
# from src.endpoints.yield_endpoint import *
from src.endpoints.yield_endpoint import *



app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

api.add_resource(YieldAPI, '/yield')
docs.register(YieldAPI)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
