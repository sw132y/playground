#!/usr/bin/env python3

import secrets
import paho.mqtt.client as paho
import json

MQTT_TOPIC_WATERFLOW = "greenhouse/waterflow"
MQTT_TOPIC_WATERTANK = "greenhouse/watertank"

client = paho.Client()

def on_publish(client, userdata, result):
    print("data published \n")
    pass

def send(topic, obj):
    client.publish(topic, json.dumps(obj))
    pass

def setup():
    client.on_publish = on_publish
    client.username_pw_set(secrets.username, secrets.password)
    client.connect(secrets.broker, secrets.port)
    pass

def get_waterflow_data():
    return {"current" : 12345, "today" : 99999 }

def get_watertank_data():
    return {"temperature" : 27, "ec" : 10, "ppm" : 100 }

setup()

send(MQTT_TOPIC_WATERFLOW, get_waterflow_data())

send(MQTT_TOPIC_WATERTANK, get_watertank_data())