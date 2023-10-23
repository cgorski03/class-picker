import boto3
import pandas as pd
import time

dynamodb = boto3.client('dynamodb')
table_name = 'CourseTable'
"""

response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'Title',  # Partition Key
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Title',
            'AttributeType': 'S'  # String
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

"""
response = dynamodb.update_table(
    TableName=table_name,
    AttributeDefinitions=[
        {
            'AttributeName': 'CAT NBR',
            'AttributeType': 'S'  # Assuming 'CAT NBR' is a number (change as needed)
        }
    ],
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'CatNbrIndex',  # Choose a unique name for the index
                'KeySchema': [
                    {
                        'AttributeName': 'CAT NBR',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'  # You can change this to 'KEYS_ONLY' or 'INCLUDE' as needed
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            }
        }
    ]
)
# import course catalog
# Replace 'your_file.xlsx' with the actual path to your Excel file.
excel_file = pd.ExcelFile('course_list.xlsx')

# Assuming the data is in the first sheet. You can specify the sheet name with the `sheet_name` parameter.
c_sheet = excel_file.sheet_names[0]
df = excel_file.parse(c_sheet)
c_list = []

for index, row in df.iterrows():
    ca = row['CA']
    ca_descr = row['CA DESCR']
    subj = row['SUBJ']
    cat_nbr = row['CAT NBR']
    title = row['TITLE']

    # Do something with the data, e.g., print it
    response = dynamodb.put_item(
    TableName=table_name,
    Item={
        'CA': {'S': ca},  # Replace with the actual value
        'CA DESCR': {'S': ca_descr},
        'SUBJ': {'S': subj},
        'CAT NBR': {'S': str(cat_nbr)},  # Assuming 'CAT NBR' is a number (use 'S' for string if needed)
        'Title': {'S': title},
        # Add more attributes as needed
    }
)

