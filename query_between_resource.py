import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "ten-examples-dynamodb-boto3"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-west-2")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
table = dynamodb.Table(TABLE_NAME)

# Use the Table resource to query all songs by artist Arturus Ardvarkian
# that are between 'Bz' and 'D'
response = table.query(
  KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian') & Key('song').between('Bz', 'D')
)
print(response['Items'])


