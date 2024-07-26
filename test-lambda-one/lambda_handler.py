import json

def lambda_handler(event, context):
    print("Hellooooooooooooo")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }