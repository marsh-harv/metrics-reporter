import requests
import json
import os

API_KEY = ''
secret_key = ''
URL = "https://api.telemetry.confluent.cloud/v1/metrics/cloud/"

def get_available_metrics():
    response = requests.get(URL + "descriptors", auth=(API_KEY, secret_key))
    print(response.status_code)
    return response

def get_topics_by_metric():
    query = 'attributes_query.json'
    response = requests.post(URL + "attributes", auth=(API_KEY, secret_key), data=open(query))
    print(response.status_code)
    return response

get_topics_by_metric()
