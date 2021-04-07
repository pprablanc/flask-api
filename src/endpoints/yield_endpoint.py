"""Endpoints, Resources and Routes"""
from flask_restful import Resource
from marshmallow import Schema, fields
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


class YieldResponseSchema(Schema):
    message = fields.Str(default='Success')


class YieldRequestSchema(Schema):
    api_type = fields.String(required=True, description="API type of awesome API")


#  Restful way of creating APIs through Flask Restful
class YieldAPI(MethodResource, Resource):
    @doc(description='My First GET Awesome API.', tags=['Awesome'])
    @marshal_with(YieldResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'My First Awesome API'}

    @doc(description='My First POST Awesome API.', tags=['Awesome'])
    @use_kwargs(YieldRequestSchema, location=('json'))
    @marshal_with(YieldResponseSchema)  # marshalling
    def post(self):
        '''
        Post method represents a get API method
        '''
        return {'message': 'My First Awesome API'}
