from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_record(dev_id, datac, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('IotDevice')

    try:
        response = table.get_item(Key={'device_id': dev_id, 'datacount': datac})

    except ClientError as e:
        print('Wrong device id entered. Please Check!')
        print(e.response['Error']['Message'])

    except:
        print('Wrong device id entered. Please Check!')
        
    else:
        return response['Item']


if __name__ == '__main__':
    a = input('Enter the device id')
    b = int(input('Enter the telemetry index: 1: Temperature, 2: Humidity'))
    record = get_record(a, b,)
    if record:
        print("Item Retrieved")
        pprint(record)
