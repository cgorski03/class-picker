import json
import boto3
import urllib.parse
"""
    Course Enrollment Lambda Function

    This Lambda function handles course enrollment for users. It checks if a user is in the system,
    verifies if a course exists, and then adds the course to the user's record if both conditions are met.

    Usage:
    To use this Lambda function, trigger it with an HTTP request to https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class, passing the course name and username in the request body as JSON.
    Example:
    - Send an HTTP POST request to your Lambda URL with the following JSON body:
      {
        "course": "YourCourseName",
        "username": "YourUsername"
      }

    Input:
    - The Lambda function expects a JSON request body containing "course" and "username" fields.
    - The "course" field should contain the desired course name (URL-encoded if needed).
    - The "username" field should contain the user's username.

    Output:
    - If the course and user exist, the function adds the course to the user's record and responds with the updated user data.
    - If the course or user is not found, it returns an appropriate error message and a 404 status code.
    - If the input is improper or missing fields, it returns a 400 status code with a message.

    CORS Headers:
    The function includes CORS (Cross-Origin Resource Sharing) headers in its response, allowing it to be called from web applications hosted on different domains.

    Error Handling:
    The function gracefully handles errors and provides informative messages along with appropriate HTTP status codes.
    """
import json
import boto3
import urllib.parse

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET"
    }
    #dev
    #request_data = json.loads(json.dumps(event['body']))
    #prod
    request_data = json.loads(event['body'])
    #check if the proper arguments have been provided
    if 'course' not in request_data or 'username' not in request_data:
        return{
            'statusCode': 400,
            'headers' : headers,
            'body': json.dumps({'message' : 'improper usage, course and username are required', 'body': request_data})

        }

    course_name = urllib.parse.unquote(request_data['course'])
    username = request_data['username']
    
    
    dynamodb = boto3.resource('dynamodb')
    courseTable = dynamodb.Table('CourseTable')
    userTable = dynamodb.Table('user-course-table')

     #prevent cors errors

    # Use the `get_item` method to retrieve the item
    response = courseTable.get_item(
        Key={'Title': course_name}  
    )


    if 'Item' in response:
            #at this point username and class both exist and you can add class to user
            # Add the course to the user's classes (string set)
        response = courseTable.update_item(
            Key={'Title': course_name},
            UpdateExpression='ADD students :new_element',
            ExpressionAttributeValues={':new_element': {username}},
        )
        response = userTable.update_item(
            Key={'username': username},
            UpdateExpression='ADD courses :new_element',
            ExpressionAttributeValues={':new_element': {course_name}},
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            updated_courses = userTable.get_item(Key={'username' : username})['Item']['courses']
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(list(updated_courses))
        }

        else:
            #user is not in the system
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'message' : 'user not found'})
            }   
    
    else:
        return {
            'statusCode': 404,
            "headers": headers,
            'body': json.dumps({'message' : 'class not found'})
        }
        