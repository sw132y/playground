#!/usr/bin/env python3
import secrets
import paho.mqtt.client as paho

def on_publish(client,userdata,result):
    print("data published \n")
    pass
client = paho.Client()
client.on_publish = on_publish
client.username_pw_set(secrets.username, secrets.password)
client.connect(secrets.broker, secrets.port)
ret = client.publish("greenhouse/waterflow/current",123)

#hassio custom sensor
#- platform: mqtt
#  name: Water Flow
#  state_topic: "greenhouse/waterflow/current"