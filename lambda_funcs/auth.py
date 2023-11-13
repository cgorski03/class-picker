import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    username = event['queryStringParameters']['username']
    password = event['queryStringParameters']['password']
    state = event['queryStringParameters']['state']
    table = dynamodb.Table(f'{state}_table')

    headers = {
        "Access-Control-Allow-Origin": "*",  # Replace '*' with specific origins if needed
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET"
    }
    
    if not username or not password:
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"message": "Bad Request"})
        }

    try:
        response = table.get_item(Key={'username': username})
        item = response.get('Item')

        if item and item.get('password') == password:
            data = {
                "statusCode": 200,
                "message": "username and password are correct"
            }
            response = {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps(data)
            }
        else:
            return {
                "statusCode": 401,
                "headers": headers,
                "body": json.dumps({"message": "Unauthorized"})
            }

    except Exception as e:
        response = {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"message": "Internal Server Error"})
        }
        
    return response
