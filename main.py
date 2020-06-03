from datetime import datetime
from time import sleep
from os import getenv

from psutil import virtual_memory, cpu_percent, disk_usage
from elasticsearch import Elasticsearch

es_password = getenv("ELASTIC_PASSWD")

client = Elasticsearch(
    cloud_id="elasticpython:c2EtZWFzdC0xLmF3cy5mb3VuZC5pbyQ3OTcwMWQyOTdiMGQ0Y2ZiOTJmMmFhZmNmNjViNjQ4ZiQ2OTdmNzVmZjJlN2E0ZGUyYWJkNzY0ZDVlZDAzYzhjZg==",
    http_auth=('elastic', es_password)
    )

id = 256

while True:

    doc = {
    "cpu": float(cpu_percent()),
    "disk": float(disk_usage('/').percent),
    "ram": float(virtual_memory().percent),
    "timestamp": datetime.utcnow()
    }

    print(doc["timestamp"])

    response = client.index(
        index = "python-new",
        id = id,
        body = doc,
        request_timeout=10
        )
    id += 1
    print(f"Resposta: {response}")
    if response["_shards"]["successful"] == 1:
        print("\nSUCCESS\n")
    sleep(10)