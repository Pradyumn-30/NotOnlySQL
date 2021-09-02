from pprint import pprint
import boto3
import numpy as np
from botocore.exceptions import ClientError


def check_status(dev_id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('IotDevice')

    try:
        response = table.get_item(Key={'device_id': dev_id, 'datacount': 1})
        temp = list(response['Item']['info'].values())
        mean_temp = np.mean(temp)
        print(f'Mean temperature for the IOT device {dev_id} is {mean_temp} degree Celcius')

    except ClientError as e:
        print(e.response['Error']['Message'])

    except:
        print('Wrong device id entered. Please Check!')

    else:
        if mean_temp > 25:
            msg = 'Turn on the sprinkler for this device'
            return msg
        else:
            msg = 'No need to turn on the sprinkler for this device'
            return msg              


if __name__ == '__main__':
    a = input('Enter the device id')
    status = check_status(a,)
    if status:
        pprint(status)
        print("Message displayed successfully")
