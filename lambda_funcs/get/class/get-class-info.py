"""
Detailed Class Information Lambda Function

This Lambda function retrieves detailed information about the classes associated with a user from DynamoDB tables.
It is triggered via an HTTP request and responds with a JSON object containing information about the user's classes.

Usage:
To use this Lambda function, trigger it with an HTTP request, passing the desired username as a query parameter.
Example:
- Send an HTTP GET request to:
  https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class/detailed?username=example_user

Input:
- The Lambda function expects the 'username' as a query parameter in the HTTP request.
  The username should be URL-encoded.

Output:
- If the user exists and has classes, the function responds with a JSON object containing detailed information about each class.
- If the user does not exist or has no classes, it responds with a "This user has no classes" message.

CORS Headers:
The function includes CORS (Cross-Origin Resource Sharing) headers in its response, allowing it to be called from web applications hosted on different domains.

Error Handling:
The function handles errors gracefully, returning a "This user has no classes" message and a 204 status code when the user does not exist or has no classes.
"""

import json
import boto3
import urllib.parse


def lambda_handler(event, context):
    # properly handle input of course name
    course_name = urllib.parse.unquote(
        event['queryStringParameters']['course'])
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CourseTable')

    # prevent cors errors
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET"
    }

    # Use the `get_item` method to retrieve the item
    response = table.get_item(
        Key={'Title': course_name}
    )
    # Check if the item was found
    if 'Item' in response:
        item = response['Item']
        return {
            'statusCode': 200,
            "headers": headers,
            'body': json.dumps(item)
        }
    else:
        return {
            'statusCode': 404,
            "headers": headers,
            'body': json.dumps({'message': 'class not found'})
        }
