#!/usr/bin/env python
# encoding: utf-8
import boto3
from flask import Flask, request
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from Helper import *
app = Flask(__name__)

# DynamoDB Profile Setup
dynamodb = boto3.resource("dynamodb", region_name='ap-northeast-2')
table = dynamodb.Table('test-dynamo')

# GET method part
@app.route('/users', methods=['GET'])
def query_records():
    params = request.get_json()
    Name = params['Name']
    PN = params['PN']
    StatusCode = 0
    try:
        response = table.get_item(
            Key={
                'Name': Name,
                'PN': PN
            }
        )
        item = response['Item']        
        StatusCode = 1
    except (ClientError, KeyError) as e:
        return ("Query Error \n check your code or query")

    if (StatusCode == 1):
        res_data = item['Zipcode']
        return (res_data)

# PUT method part
@app.route('/users', methods=['PUT'])
def create_record():
    # Request value save
    params = request.get_json()
    Name = params['Name']
    PN = params['PN']
    Zipcode = params['Zipcode']
    # Query to DynamoDB
    response = table.put_item(
    Item={
            'Name': Name,
            'PN': PN,
            'Zipcode': Zipcode
        }
    )
    return ("Edit Complete!!")

# POST method part
@app.route('/users', methods=['POST'])
def update_record():
    # Request value save
    params = request.get_json()
    Name = params['Name']
    PN = params['PN']
    Zipcode = params['Zipcode']
    # Query to DynamoDB
    response = table.put_item(
    Item={
            'Name': Name,
            'PN': PN,
            'Zipcode': Zipcode
        }
    )
    return ("Write Complete!!")

# DELETE method part
@app.route('/users', methods=['DELETE'])
def delte_record():
    # Request value save
    params = request.get_json()
    Name = params['Name']
    PN = params['PN']
    # Query to DynamoDB
    response = table.delete_item(
        Key={
            'Name': Name,
            'PN': PN
        }
    )
    return ("Delete Complete!!")

# Healthcheck part
@app.route('/health', methods=['GET'])
def health_check():
    health = '{ "status" : 200 } '
    health_data = json.loads(health)
    return (health_data)

app.run(host='0.0.0.0', port=8080, debug=True)