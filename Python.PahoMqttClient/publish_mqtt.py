#!/usr/bin/env python3

import paho.mqtt.client as paho
broker="___"
port=1883
username="___"
password="___"

def on_publish(client,userdata,result):
    print("data published \n")
    pass
client= paho.Client()
client.on_publish = on_publish
client.username_pw_set(username, password)
client.connect(broker,port)
ret = client.publish("greenhouse/waterflow/current",123)

#hassio custom sensor
#- platform: mqtt
#  name: Water Flow
#  state_topic: "greenhouse/waterflow/current"