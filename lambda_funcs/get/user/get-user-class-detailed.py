import boto3
import json 
from urllib.parse import unquote

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST"
    }
    
    
    # Takes Username and course
    username = unquote(event['queryStringParameters']['username'])
    
    user_course_table = boto3.resource('dynamodb').Table('user-course-table')
    course_table = boto3.resource('dynamodb').Table('CourseTable')
    
    response = user_course_table.get_item(
        Key={'username' : username}
    )
    
    if 'Item' in response:
        if 'courses' not in response['Item']:
            return {
                'statusCode': 204,
                'headers': headers,
                'body': 'This user has no classes'
            }
        courses = response['Item']['courses']
        course_info_list = []
        for course in courses:
            response = course_table.get_item(
                Key = {'Title' : course},
                ProjectionExpression="#Title, #CA, #CAT_NBR, #days_meet, #end_time, #start_time, #SUBJ",
                ExpressionAttributeNames={
                    "#Title": "Title",
                    "#CA": "CA",
                    "#CAT_NBR": "CAT NBR",
                    "#days_meet": "days_meet",
                    "#end_time": "end_time",
                    "#start_time": "start_time",
                    "#SUBJ": "SUBJ"
                }
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
            'statusCode': 204,
            'headers': headers,
            'body': 'This user has no classes'
        }   
