import json
import boto3
import urllib.parse
"""
    Course Information Lambda Function

    This Lambda function retrieves information about a course from a DynamoDB table.
    It is triggered via an HTTP request and responds with information about the course if found,
    or a "class not found" message if the course is not in the database.

    Usage:
    To use this Lambda function, trigger it with an HTTP request, passing the desired course name as a query parameter.
    Example:
    - Send an HTTP GET request to:
      https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/search/get-info

    Input:
    - The Lambda function expects the 'course' name as a query parameter in the HTTP request.
      The course name should be URL-encoded.

    Output:
    - If the course is found, the function responds with a JSON object containing course information.
    - If the course is not found, it responds with a "class not found" message.

    CORS Headers:
    The function includes CORS (Cross-Origin Resource Sharing) headers in its response, allowing it to be called from web applications hosted on different domains.

    Error Handling:
    The function handles errors gracefully, returning a "class not found" message and a 404 status code when a requested course is not in the database.
    """
def lambda_handler(event, context):
    #properly handle input of course name
    course_name = urllib.parse.unquote(event['queryStringParameters']['course'])
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CourseTable')

    #prevent cors errors
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
            
            'body': json.dumps({'message' : 'class not found'})
        }
    