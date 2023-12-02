import json
import boto3
"""
Lambda function to check if adding a course to a user's schedule
would cause time conflicts with existing enrolled courses.

Parameters:
    POST request with 'username' (versionState.getuserID.value) and the course to be added

Returns:
- dict: Response containing statusCode, headers, and body.
    - If successful and no conflicts: statusCode 200.
    - If user not found: statusCode 404.
    - If time conflicts with existing courses:
    - 409: Direct time conflict.
    - 199: Start or end time conflict with existing course.
    - In body['course'] function returns the course from the user's schedule with with the course to be added conflicts with

Response Body Format:
- For success:
    {"message": "This class can be added without conflicts"}
- For conflicts:
    {"message": "Conflict message", "course": conflicting_course_info}
- For user not found:
    {"message": "user not found"}

Example Usage:
- Request:
    {"username": "user123", "course": "Math101"}
- Response (No conflicts):
    {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*", ...}, "body": '{"message": "This class can be added without conflicts"}'}
- Response (Direct time conflict):
    {"statusCode": 409, "headers": {"Access-Control-Allow-Origin": "*", ...}, "body": '{"message": "This class takes place at the same time as another class you are enrolled in", "course": {"Title": "ConflictingCourse", ...}}'}

"""
import json
import boto3

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST"
    }
    request_data = json.loads(json.dumps(event['body']))
    # Takes Username and course
    username = request_data['username']
    target_course_name = request_data['course']
    
    
    user_course_table = boto3.resource('dynamodb').Table('user-course-table')
    course_table = boto3.resource('dynamodb').Table('CourseTable')
    
    target_course_info = course_table.get_item(
        Key = {'Title' : target_course_name}
        )['Item']
        
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
            course_data = response['Item']
            if course_data['days_meet'] == target_course_info['days_meet']:
                if course_data['start_time'] == target_course_info['start_time']:
                    #the courses directly conflict
                    return {
                        'statusCode': 409,
                        'headers': headers,
                        'body': json.dumps({
                            'message' : 'This class takes place at the same time as another class you are enrolled in',
                            'course': course_data
                        })
                    }
                if course_data['end_time'] == target_course_info['start_time']:
                    return {
                        'statusCode': 199,
                        'headers': headers,
                        'body': json.dumps({
                            'message' : 'This class starts at the same time another class you are enrolled in ends',
                            'course': course_data
                        })
                    }
                if course_data['start_time'] == target_course_info['end_time']:
                    return {
                        'statusCode': 199,
                        'headers': headers,
                        'body': json.dumps({
                            'message' : 'This class ends at the same time another class you are enrolled in starts',
                            'course': course_data
                        })
                    }
        print("all good")
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
            'message' : 'This class can be added without conflicts',
            })
        }
            
        
    else:
        #user does not exist
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'message' : 'user not found'})
            }   
