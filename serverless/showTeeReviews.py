import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def showTeeReviews(id):
    try:
        # Credentials to access DynamoDB is associated with IAM policy 
        # This IAM policy inturn is tied to Lambda for proper permission access
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('runcystees')

        resp = table.get_item(Key={"id": id})

        if resp.get('Item') == None:
            return {"result": False}

        return {"result": True, "reviews": resp['Item']['reviews']}
    except ClientError as e:
        return {"result": "Error occurred"}
        print("Error occurred - showTeeReviews(", id, ") - ", e.response)

def lambda_handler(event, context):
    id = ""
    if 'id' in event:
        id = event['id']

    teeinfo = showTeeReviews(id)
    return teeinfo
