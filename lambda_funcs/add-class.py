import json
import boto3
import urllib.parse

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "POST"
    }
    
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
        response = userTable.update_item(
            Key={'username': username},
            UpdateExpression='ADD courses :new_element',
            ExpressionAttributeValues={':new_element': {course_name}},
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(list(userTable.get_item(Key={'username' : username})['Item']['courses']))
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
        