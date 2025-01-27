from flask import Flask, Response
import requests
import prometheus_client
from prometheus_client.core import GaugeMetricFamily, REGISTRY

app = Flask(__name__)

SELENIUM_HUB_URL = "http://selenium-hub.selenium.svc.cluster.local:4444"

class SeleniumQueueSizeCollector:
    def collect(self):
        try:
            response = requests.get(f"{SELENIUM_HUB_URL}/se/grid/newsessionqueue/queue")
            response.raise_for_status()
            queue = response.json()
            queue_size = len(queue['value'])
            gauge = GaugeMetricFamily("selenium_queue_size", "Number of pending sessions in the Selenium Grid queue")
            gauge.add_metric([], queue_size)
            yield gauge
        except Exception as e:
            print(f"Error fetching queue size: {e}")

REGISTRY.register(SeleniumQueueSizeCollector())

@app.route("/metrics")
def metrics():
    return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)