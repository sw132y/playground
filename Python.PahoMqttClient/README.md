# Playground of sending MQTT messages from Python to Hassio via MQTT
Python MQTT Client

# How to run?
```
python -m pip install --upgrade pip
pip install -r requirements.txt
python publish_mqtt.py
python subscribe_mqtt.py
```

# Setup
Create `secrets.py` file and fill data
```
broker="ip_address_of_your_mqtt_server"
port=1883
username="mqtt_username"
password="mqtt_password"
```

# Handle MQTT data in Hassio
Define custom sensor. Add into `configuration.yaml` line:
```
sensor: !include customize_sensors.yaml
```

Define custom MQTT sensors in `customize_sensors.yaml`
```
- platform: mqtt
  name: Current waterflow
  icon: mdi:water
  state_topic: "greenhouse/waterflow"
  unit_of_measurement: 'l/min'
  value_template: "{{ value_json.current }}"
  
- platform: mqtt
  name: Today waterflow
  icon: mdi:water
  state_topic: "greenhouse/waterflow"
  unit_of_measurement: 'l/min'
  value_template: "{{ value_json.today }}"
```

Display sensor values in lovelace:
```
- type: entities
  show_header_toggle: false
  title: Water flow
  entities:
    - sensor.current_waterflow
    - sensor.today_waterflow
```