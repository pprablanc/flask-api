"""Endpoints, Resources and Routes"""
from flask_restful import Resource
from marshmallow import Schema, fields
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

from src.functions import load_data
# load data
df = load_data()


class YieldSchema(Schema):
    id = fields.Integer()
    type = fields.Str()
    time = fields.Integer()
    yield_mean = fields.Float()
    yield_map = fields.List(fields.List(fields.Float()))

class YieldMeanSchema(Schema):
    id = fields.Integer()
    time = fields.Integer()
    type = fields.Str()
    yield_mean = fields.Float()

class YieldMeanListSchema(Schema):
    yields = fields.List(fields.Nested(YieldMeanSchema))


# Restful way of creating APIs through Flask Restful
class YieldAPI(MethodResource, Resource):
    @doc(description='GET yield API.', tags=['yield'])
    @marshal_with(YieldSchema)  # marshalling
    def get(self, id):
        '''
        Get method to get all data.
        '''
        # res = [{'id': row['id'], 'time': row['time'], 'type': row['cereal'], 'yield_mean': row['yield_mean'], 'yield_map': [[float(row_map) for row_map in col_map] for col_map in row['yield_map'].data]} for index, row in df.iterrows()]
        res = df.iloc[id][['id', 'type', 'time', 'yield_map']]
        res['yield_map'] = res['yield_map'].data
        return res

class YieldMeanTypeAPI(MethodResource, Resource):
    @doc(description='GET mean yield for a given type of cereal API.', tags=['yield/mean/type/<id>'])
    @marshal_with(YieldMeanListSchema)  # marshalling
    def get(self, typeId):
        '''
        Get method to get all data.
        '''
        tmp = df.groupby(['type']).get_group(typeId)[['id', 'time', 'type', 'yield_mean']]
        return {'yields': [tmp.iloc[i] for i in range(len(tmp))]}
