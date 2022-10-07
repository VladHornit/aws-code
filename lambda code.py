import pandas as pd
import boto3
import os
import json
import time
import requests as r

MYBUCKET = 'my-bucket-name'

def lambda_handler(event, context):
    client = boto3.client('s3')
    print(1)

    # Data to be written
    l = r.get('https://www.binance.com/api/v1/depth?symbol=NMRBTC&limit=100')
    # Serializing json

    df = pd.DataFrame(json.loads(l.content))

    #create name
    name = 'vlad.csv'
    lambda_path = "/tmp/" + name

    df = pd.concat([pd.DataFrame(df.bids.tolist(), columns=['bid_price',
    'bid_qty']),
    pd.DataFrame(df.asks.tolist(), columns=['ask_price',
    'ask_qty'])], 1)

    object_name = "test"
    bucket = MYBUCKET
    df.to_csv(lambda_path, index=False)
        client.upload_file(Filename=lambda_path, Bucket=bucket, Key=object_name)
    print(1)
    return {}
