import requests
from datadog import initialize, api
import time
from random import randint

api_key = "a6dd994468ec7c4cf1bfd263087a26c9"

def brightnessMetric():
    metric = randint(25, 100)

    if randint(0,20) == 7:
        metric = 0

    return metric

def tempMetric():
    URL = "https://api.darksky.net/forecast/bec279e1003d1670b56ac052aeafb185/33.116455,-96.884606"
    r = requests.get(url = URL)
    data = r.json()
    temp = data["currently"]["temperature"]
    print('Current Temperature ['+str(temp)+']')
    return temp

options = {
    'api_key': '2941097c17d0de885520f96439be776b',
    'app_key': '50cc6a742a2d7f3cfcda99a54e8bc932ced548c7'
}

initialize(**options)

while(true):
    #Sensor Metric
    api.Metric.send(
        metric='sensor.brightness',
        points=brightnessMetric(),
        tags=["location:SellariSystemAPI"]
    )

    #Temp Metric
    api.Metric.send(
        metric='sensor.temperature',
        points=tempMetric(),
        tags=["location:SellariSystemAPI"]
    )
    time.sleep(10)
