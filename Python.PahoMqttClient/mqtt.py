#!/usr/bin/env python3

import json
import secrets
import paho.mqtt.client as paho

client = paho.Client()

def on_publish(client, userdata, result):
    print(f"MQTT data published \n")
    pass

def send(topic, obj):
    client.publish(topic, json.dumps(obj))
    pass

def setup():
    print(f"MQTT start connection to the server {secrets.broker}:{secrets.port} \n")
    client.on_publish = on_publish
    client.username_pw_set(secrets.username, secrets.password)
    client.connect(secrets.broker, secrets.port)
    pass

setup()