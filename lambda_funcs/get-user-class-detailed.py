import boto3
import json 
from urllib.parse import unquote
"""
# User Courses Lambda Function

## Overview

This AWS Lambda function retrieves the courses associated with a user from a DynamoDB table. It is designed for integration with an API Gateway to enable HTTP GET requests.

## Usage

### Endpoint
https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class/detailed

### Request

- Method: `GET`
- Headers: `Content-Type: application/json`

### Query Parameters

- `username` (required): The unique identifier of the user whose courses need to be retrieved.

### Response

- If the user is found:
  - Status Code: `200 OK`
  - Body: JSON object containing the courses associated with the user and their attributes.
  - the response will include ALL attributes of each course


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
def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST"
    }
    #testing
    #request_data = json.loads(json.dumps(event['body']))
    
    #prod
    #request_data = json.loads(event['body'])
    
    # Takes Username and course
    username = unquote(event['queryStringParameters']['username'])
    
    user_course_table = boto3.resource('dynamodb').Table('user-course-table')
    course_table = boto3.resource('dynamodb').Table('CourseTable')
    
    response = user_course_table.get_item(
        Key={'username' : username}
    )
    
    if 'Item' in response:
        
        courses = response['Item']['courses']
        course_info_list = []
        for course in courses:
            response = course_table.get_item(
                Key = {'Title' : course}
                )
            course_info_list.append(response['Item'])

        print("all good")
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
            'courses' : json.dumps(course_info_list),
            })
        }
            
        
    else:
        #user does not exist
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'message' : 'user not found'})
            }   
