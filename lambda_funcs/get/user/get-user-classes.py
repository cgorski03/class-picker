"""
# User Courses Lambda Function

## Overview

This AWS Lambda function retrieves the courses associated with a user from a DynamoDB table. It is designed for integration with an API Gateway to enable HTTP GET requests.

## Usage

### Endpoint
https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class

### Request

- Method: `GET`
- Headers: `Content-Type: application/json`

### Query Parameters

- `username` (required): The unique identifier of the user whose courses need to be retrieved.

### Response

- If the user is found:
  - Status Code: `200 OK`
  - Body: JSON array containing the courses associated with the user.

    Example: `["Course1", "Course2", "Course3"]`

- If the user is not found or has no courses:
  - Status Code: `404 Not Found`
  - Body: JSON object with an error message.

    Example: `{"message": "no classes found"}`

## CORS Configuration

- Headers:
  - `Access-Control-Allow-Origin: *`
  - `Access-Control-Allow-Headers: Content-Type`
  - `Access-Control-Allow-Methods: OPTIONS, GET`

"""
import json
import boto3

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, GET"
    }
    
    #check if the proper arguments have been provided
    if 'username' not in event['queryStringParameters']:
        return{
            'statusCode': 400,
            'headers' : headers,
            'body': json.dumps({'message' : 'improper usage, username are required'})
        }

    username = event['queryStringParameters']['username']
    
    
    dynamodb = boto3.resource('dynamodb')
    userTable = dynamodb.Table('user-course-table')

    response = userTable.get_item(
        Key={'username' : username}
    )
    if 'Item' in response:
        return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(list(userTable.get_item(Key={'username' : username})['Item']['courses']))
        }
    else:
        #user has no classes
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'message' : 'no classes found'})
            }   




