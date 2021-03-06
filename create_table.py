import boto3

def create_devices_table(dynamodb = None):
    dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:8000")
    print(list(dynamodb.tables.all()))
    table = dynamodb.create_table(
        TableName = 'IotDevice',
        KeySchema = [
            {
               'AttributeName': 'device_id',
               'KeyType': 'HASH'
            },
            {
                'AttributeName': 'datacount',
                'KeyType': 'RANGE'
            }           
        ],
        AttributeDefinitions = [
            {
               'AttributeName':'device_id',
               'AttributeType':'S'
            },
            {
                'AttributeName':'datacount',
                'AttributeType':'N'
            },
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits':10,
            'WriteCapacityUnits':10
        }
    )
    return table
    
if __name__ == '__main__':
    device_table = create_devices_table()
    print('Status:', device_table.table_status)