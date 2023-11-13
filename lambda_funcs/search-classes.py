import json
import boto3
"""
Course Search Lambda Function

Description:
This AWS Lambda function searches for courses based on provided keywords and returns the matching courses.

Usage:
To use this Lambda function, trigger it with an HTTP request, passing the search query in the query parameters.
Example:
- Send an HTTP GET request to your Lambda URL with the search query:
  `https://4jui141iri.execute-api.us-east-1.amazonaws.com/dev/search`

Input:
- Query parameters:
  - `search`: The search query containing keywords separated by "%20" for space.

Output:
- The Lambda function returns a JSON response with the matching courses or a "not found" message with a 404 status code if no matching courses are found.

CORS (Cross-Origin Resource Sharing):
- This function handles CORS headers to allow cross-origin requests.

Response:
- If courses are found, the function returns a JSON array of matching courses with a 200 status code.
- If no courses are found, the function returns a "not found" message with a 404 status code.
"""

def lambda_handler(event, context):
    lowercase_words = set('to', 's', 'a', 'its', 'before', 'liberalism', 'with', 'of', 'since', 'for', 'from', 'as', 'into', 'and', 'through', 'the', 'on', 'de', 'western', 'present', 'in', 'o')
    dynamodb = boto3.resource('dynamodb')
    search = event['queryStringParameters']['search']
    table = dynamodb.Table('CourseTable')
    tokens = search.split('%20') #split the string at space characters to find keywords
    
    filtered_keywords = [word.title() if word.lower() not in lowercase_words else word for word in tokens]
    #prevent cors errors
    headers = {
        "Access-Control-Allow-Origin": "*",  
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS, POST, GET"
    }
    
    
    # Build the filter expression dynamically with multiple keywords
    filter_expression = ' and '.join([f'contains(Title, :keyword{i})' for i, keyword in enumerate(filtered_keywords)])
    expression_attribute_values = {f':keyword{i}': keyword for i, keyword in enumerate(filtered_keywords)}
    
    print(filter_expression)
    # Perform the scan operation
    response = table.scan(
        FilterExpression=filter_expression,
        ExpressionAttributeValues=expression_attribute_values
    )


    # Retrieve the classes that match the scan
    classes = response.get('Items', [])

    if classes is None: #classes not found. Return 404 not found
        response = {
                "statusCode": 404,
                "headers": headers,
                "body": json.dumps({'message' : 'classes with the given keywords do not exist'})
            }
    else: #classes found return the classes
        response = { 
                    "statusCode": 200,
                    "headers": headers,
                    "body": json.dumps(classes)
                }

    return response
    