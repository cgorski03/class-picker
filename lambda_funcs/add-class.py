import json
import boto3
import urllib.parse

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET"
    }
    request_data = json.loads[event['body']]
    #check if the proper arguments have been provided
    if 'course' not in event or 'username' not in request_data:
        return{
            'statusCode': 400,
            'headers' : headers,
            'body': json.dumps({'message' : 'improper usage, course and username are required'}, json.dumps(request_data['body']))

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

    # Check if the item was found
    if 'Item' in response:
        item = response['Item']
        response = userTable.get_item(
            Key={'username' : username}
        )
        if 'Item' in response:
            #at this point username and class both exist and you can add class to user
            response = userTable.update_item(
                Key={'username': username},
                UpdateExpression='SET classes = list_append(classes, :new_element)',
                ExpressionAttributeValues={':new_element': [course_name]},
                ReturnValues='ALL_NEW'  # If you want to return the updated item
            )

            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                print(response['Attributes'])
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(response['Attributes'])
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
    