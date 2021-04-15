"""Endpoints, Resources and Routes"""
from flask import render_template, Response
from flask_restful import Resource
from marshmallow import Schema, fields
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

from src.settings import df



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


class TypeListSchema(Schema):
    types = fields.List(fields.Str())


# Restful way of creating APIs through Flask Restful
class YieldAPI(MethodResource, Resource):
    @doc(description='GET yield API.', tags=['yield'])
    @marshal_with(YieldSchema)  # marshalling
    def get(self, id):
        '''
        Get method to get yield data based on id.
        '''
        # res = [{'id': row['id'], 'time': row['time'], 'type': row['cereal'], 'yield_mean': row['yield_mean'], 'yield_map': [[float(row_map) for row_map in col_map] for col_map in row['yield_map'].data]} for index, row in df.iterrows()]
        res = df.iloc[id][['id', 'type', 'time', 'yield_map']]
        res['yield_map'] = [list(row) for row in res['yield_map'].data]
        return res

class YieldMeanTypeAPI(MethodResource, Resource):
    @doc(description='GET mean yield for a given type of cereal API.', tags=['yield/mean/type/<id>'])
    @marshal_with(YieldMeanListSchema)  # marshalling
    def get(self, typeId):
        '''
        Get method to get mean yield and timestamp for a given type of cereal.
        '''
        tmp = df.groupby(['type']).get_group(typeId)[['id', 'time', 'type', 'yield_mean']]
        return {'yields': [tmp.iloc[i] for i in range(len(tmp))]}

class TypeCerealAPI(MethodResource, Resource):
    @doc(description='GET mean yield for a given type of cereal API.', tags=['yield/mean/type/<id>'])
    @marshal_with(TypeListSchema)  # marshalling
    def get(self):
        '''
        Get method to get all data.
        '''
        return {'types': list(df['type'].unique())}


class DashboardAPI(MethodResource, Resource):
    @doc(description='GET dashboard API.', tags=['dashboard'])
    def get(self):
        return Response(render_template("dashboard.html", template_folder='src/template'), mimetype='text/html')
