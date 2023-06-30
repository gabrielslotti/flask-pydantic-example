from flask import Flask, jsonify, request
from enum import Enum
from typing import Dict, Optional
from pydantic import BaseModel
from flask_pydantic import validate


app = Flask(__name__)


class StatusEnum(Enum):
    ok = 'ok'
    error = 'error'


class BaseResponseModel(BaseModel):
    status: StatusEnum
    message: str


@app.route("/")
def hello_world() -> BaseResponseModel:
    return jsonify(status='ok', message='Hello, World!'), 200


############################
# Validate URL Path Params #
############################

@app.route('/name/<name>', methods=['GET'])
@validate()
def get_name(name: str) -> BaseResponseModel:
    return jsonify(status='ok', message=f'My name is {name}!')

@app.route('/number/<number>', methods=['GET'])
@validate()
def get_number(number: int) -> BaseResponseModel:
    return jsonify(status='ok', message=f'My number is {number}!')


#############################
# Validate URL Query Params #
#############################

class QueryModel(BaseModel):
    age: int
    first_name: str
    last_name: str

@app.route('/query', methods=['GET'])
@validate()
def query(query: QueryModel) -> BaseResponseModel:
    return BaseResponseModel(
        status='ok',
        message=f'My name is {query.first_name} {query.last_name} and I am {query.age}!'
    )


#########################
# Validate request body #
#########################

class BodyModel(BaseModel):
    age: int
    first_name: str
    last_name: str


@app.route('/body', methods=['POST'])
@validate()
def body(body: BodyModel) -> BaseResponseModel:
    return BaseResponseModel(
        status='ok',
        message=f'My name is {body.first_name} {body.last_name} and I am {body.age}!'
    )


##################################
# Validate body and query params #
##################################

@app.route('/body_query', methods=['POST'])
@validate(query=QueryModel, body=BodyModel, on_success_status=201)
def body_query() -> BaseResponseModel:
    return BaseResponseModel(
        status='ok',
        message='Body and query params are OK!'
    )


########################################
# Validate Query, Body and Path params #
########################################

@app.route('/body_query_path/<param>', methods=['POST'])
@validate()
def body_query_path(param: str, query=QueryModel, body=BodyModel) -> BaseResponseModel:
    return BaseResponseModel(
        status='ok',
        message='Body, Query and Path params are OK!'
    )