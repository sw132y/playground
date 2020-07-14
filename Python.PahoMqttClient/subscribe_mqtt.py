#!/usr/bin/env python3

import mqtt

MQTT_TOPIC_WATERPUMP = "greenhouse/waterpump"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

mqtt.client.on_message = on_message
mqtt.subscribe(MQTT_TOPIC_WATERPUMP)

mqtt.client.loop_forever()