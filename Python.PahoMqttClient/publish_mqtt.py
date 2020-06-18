#!/usr/bin/env python3

import mqtt

MQTT_TOPIC_WATERFLOW = "greenhouse/waterflow"
MQTT_TOPIC_WATERTANK = "greenhouse/watertank"

def get_waterflow_data():
    return {"current" : 12345, "today" : 99999 }

def get_watertank_data():
    return {"temperature" : 27, "ec" : 10, "ppm" : 100 }

mqtt.send(MQTT_TOPIC_WATERFLOW, get_waterflow_data())
mqtt.send(MQTT_TOPIC_WATERTANK, get_watertank_data())