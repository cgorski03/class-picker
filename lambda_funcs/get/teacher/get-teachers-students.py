"""
Teacher's Class Information Lambda Function

This Lambda function retrieves information about the classes associated with a teacher from DynamoDB tables.
It will return a list of courses the teacher is teaching and the students enrolled in the course currently.

Endpoint:
- https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class/teacher

Usage:
To use this Lambda function, trigger it with an HTTP GET request, passing the 'username' of the teacher as a query parameter.
Example:
- Send an HTTP GET request to:
  https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/class/teacher?username=example_teacher

Input:
- The Lambda function expects the 'username' as a query parameter in the HTTP request.
  The username should be URL-encoded.

Output:
- If the teacher exists and has classes, the function responds with a JSON object containing information about each class.
- If the teacher does not exist or has no classes, it responds with a JSON object containing a 'message' key indicating 'no classes found'.

CORS Headers:
The function includes CORS (Cross-Origin Resource Sharing) headers in its response, allowing it to be called from web applications hosted on different domains.

DynamoDB Tables Used:
- 'user-course-table': Stores the mapping of users to their enrolled courses.
- 'CourseTable': Stores detailed information about each course.

Error Handling:
The function handles errors gracefully, returning a JSON object with a 'message' key indicating 'improper usage' and a 400 status code when the required query parameter is missing.
If the teacher does not exist or has no classes, it returns a JSON object with a 'message' key indicating 'no classes found' and a 404 status code.

Note:
Ensure that the DynamoDB tables are properly configured with the required attributes ('username' in 'user-course-table' and 'Title' in 'CourseTable').
"""
import json
import boto3
import urllib.parse


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
    
    username = urllib.parse.unquote(event['queryStringParameters']['username'])
    
    
    dynamodb = boto3.resource('dynamodb')
    courseTable = dynamodb.Table('CourseTable')
    userTable = dynamodb.Table('user-course-table')

    response = userTable.get_item(
        Key={'username' : username}
    )
    if 'Item' in response:
        if 'courses' not in response['Item']:
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'message' : 'no classes found'})
            }
        
        courses_data = []
        for course in response['Item']['courses']:
            students_response = courseTable.get_item(Key={'Title': course})

            if 'Item' in students_response:
                students_list = students_response['Item'].get('students', [])
                course_data = {"title": course, "students": list(students_list)}
                courses_data.append(course_data)
        print(courses_data)
        jsonobj = json.dumps({"courses": courses_data})
        print(jsonobj)
        
        return {
            'statusCode': 200,
            'headers': headers,  
            'body': json.dumps({"courses": courses_data})
        }
    else:
        #user does not exist
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'message' : 'no classes found'})
            }   




