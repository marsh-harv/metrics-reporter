import metrics_api
import time

while True:
    metrics_api.get_sent_bytes_prod()
    metrics_api.get_received_bytes_prod()
    metrics_api.get_sent_bytes_dev()
    metrics_api.get_received_bytes_dev()
    metrics_api.retained_bytes_dev()
    time.sleep(300)
