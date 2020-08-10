import boto3
from boto3.dynamodb.conditions import Key, Attr
import sys
import os

table_name=os.environ['TABLE_NAME'] # dynamodb
end_point=os.environ['END_POINT']   # http://172.19.0.3:8000

dynamodb = boto3.resource('dynamodb',endpoint_url=end_point)

def table_create():
    res = dynamodb.create_table(
        TableName = table_name,
        AttributeDefinitions = [
                {
                    "AttributeName": "id",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "tm",
                    "AttributeType": "N"
                }
            ],
        KeySchema = [
                {
                    "AttributeName": "id",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "tm",
                    "KeyType": "RANGE"
                }
            ],
            ProvisionedThroughput = {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1
                    }
    )
    return "table_create ok"

def put_table_data():
    table = dynamodb.Table(table_name)
    demo=[
        [1234,"a",123,"v1"],
        [1235,"b",124,"v2"],
        [1235,"a",125,"v3"],
        [1236,"c",125,"v2"],
        [1237,"a",126,"v1"]
    ]

    try:
        for i in demo:
            a={}
            a["tm"] = i[0]
            a["id"] = i[1]
            a["v1"] = i[2]
            a["v2"] = i[3]           
            table.put_item(
               Item=a
            )
    except Exception as e:
        print("Error executing batch_writer",e)
    return "put_table_data ok"


def get_table_data():
    return dynamodb.Table(table_name).scan()['Items']

def get_tables():
    return list(dynamodb.tables.all())

def table_delete():
    table = dynamodb.Table(table_name)
    table.delete()
    return "table_delete ok"


if __name__ == '__main__':
    print(table_create())
    print(get_tables())
    print(put_table_data())
    print(get_table_data())
    print(table_delete())
    print(get_tables())

