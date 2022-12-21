import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "ten-examples-dynamodb-boto3"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-west-2")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
table = dynamodb.Table(TABLE_NAME)

# Use the DynamoDB client get item method to get a single item
response = dynamodb_client.get_item(
    TableName=TABLE_NAME,
    Key={
        'artist': {'S': 'Arturus Ardvarkian'},
        'song': {'S': 'Carrot Eton'}
    }
)
print(response['Item'])