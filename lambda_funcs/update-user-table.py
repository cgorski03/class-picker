import json
import boto3

def lambda_handler(event, context):
    """
    Will ensure that all users in the user password table are also in the user class table
    """

    dynamodb = boto3.resource('dynamodb')
    new_user_id = event['Records'][0]['dynamodb']['Keys']['username']['S']
    table = dynamodb.Table('user-course-table')

    item = {
        'username': new_user_id,
        'classes': {}
    }

    response = table.put_item(Item=item)

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Item was successfully added to the table.")
        return {
            'statusCode': 200,
            'body': json.dumps(event)
        }
    else:
        print("Failed to add the item to the table.")
        return {
            'statusCode': 500,
            'body': json.dumps(event)
        }