import requests
from datetime import datetime, timedelta

now = datetime.now()
TIME = format(now - timedelta(hours=3), "%H:%M:%S")
DATE = now.strftime("%Y-%m-%d")
INTERVAL_TIME = format(now - timedelta(minutes=30), "%H:%M:%S")
API_KEY = ''
secret_key = ''
URL = "https://api.telemetry.confluent.cloud/v1/metrics/cloud/"


def get_available_metrics():
    response = requests.get(URL + "descriptors", auth=(API_KEY, secret_key))
    print(response.status_code)
    return response


def get_received_bytes_dev():
    query = {
        "aggregations": [
            {
                "agg": "SUM",
                "metric": "io.confluent.kafka.server/received_bytes"
            }
        ],
        "filter": {
            "filters": [
                {
                    "field": "metric.label.cluster_id",
                    "op": "EQ",
                    "value": "lkc-"
                }
            ],
            "op": "AND"
        },
        "granularity": "PT1M",
        "group_by": [
            "metric.label.topic"
        ],
        "intervals": [
            f"{DATE}T{TIME}-00:00/{DATE}T{INTERVAL_TIME}-00:00"
        ],
        "limit": 25
    }
    response = requests.post(URL + "query", auth=(API_KEY, secret_key), json=query)
    print(response.status_code)
    return response


def get_sent_bytes_dev():
    query = {
        "aggregations": [
            {
                "agg": "SUM",
                "metric": "io.confluent.kafka.server/sent_bytes"
            }
        ],
        "filter": {
            "filters": [
                {
                    "field": "metric.label.cluster_id",
                    "op": "EQ",
                    "value": "lkc-"
                }
            ],
            "op": "AND"
        },
        "granularity": "PT1M",
        "group_by": [
            "metric.label.topic"
        ],
        "intervals": [
            f"{DATE}T{TIME}-00:00/{DATE}T{INTERVAL_TIME}-00:00"
        ],
        "limit": 25
    }
    response = requests.post(URL + "query", auth=(API_KEY, secret_key), json=query)
    print(response.status_code)
    return response


def get_received_bytes_prod():
    query = {
        "aggregations": [
            {
                "agg": "SUM",
                "metric": "io.confluent.kafka.server/received_bytes"
            }
        ],
        "filter": {
            "filters": [
                {
                    "field": "metric.label.cluster_id",
                    "op": "EQ",
                    "value": "lkc-"
                }
            ],
            "op": "AND"
        },
        "granularity": "PT1M",
        "group_by": [
            "metric.label.topic"
        ],
        "intervals": [
            f"{DATE}T{TIME}-00:00/{DATE}T{INTERVAL_TIME}-00:00"
        ],
        "limit": 25
    }
    response = requests.post(URL + "query", auth=(API_KEY, secret_key), json=query)
    print(response.status_code)
    return response


def get_sent_bytes_prod():
    query = {
        "aggregations": [
            {
                "agg": "SUM",
                "metric": "io.confluent.kafka.server/sent_bytes"
            }
        ],
        "filter": {
            "filters": [
                {
                    "field": "metric.label.cluster_id",
                    "op": "EQ",
                    "value": "lkc-"
                }
            ],
            "op": "AND"
        },
        "granularity": "PT1M",
        "group_by": [
            "metric.label.cluster_id"
        ],
        "intervals": [
            f"{DATE}T{TIME}-00:00/{DATE}T{INTERVAL_TIME}-00:00"
        ],
        "limit": 25
    }
    response = requests.post(URL + "query", auth=(API_KEY, secret_key), json=query)
    print(response.status_code)
    return response


def retained_bytes_dev(path):
    query = path
    response = requests.post(URL + "query", auth=(API_KEY, secret_key), json=query)
    print(response.status_code)
    return response
