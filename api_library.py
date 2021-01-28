import requests
import json 
import os

API_KEY = 'M3CYBVQQ243F36OJ'
secret_key = 'XSzohRenAfmqEHHAA4d9hJV66cm5KRjxUuHGlh89xtX4VqaLmsw7aeo6FZimXoH6'
URL = "https://api.telemetry.confluent.cloud/v1/metrics/cloud/"

def get_available_metrics():
    response = requests.get(URL + "descriptors", auth=(API_KEY, secret_key))
    print(response.status_code)
    return response

def get_topics_by_metric():
    query = '{}/attributes_query.json'.format(os.path.dirname(__file__))
    response = requests.post(URL + "descriptors", auth=(API_KEY, secret_key), data=open(query))
    print(response.status_code)
    return response

get_topics_by_metric()
