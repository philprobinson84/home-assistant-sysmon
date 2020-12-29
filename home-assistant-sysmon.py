import paho.mqtt.client as mqtt 
import socket
import json
import psutil
from time import sleep

mqttBroker ="192.168.1.187" 
room = socket.gethostname()

client = mqtt.Client(f"{room} SysMon")
client.connect(mqttBroker)
client.loop_start()

def registerSensors():
    config = {"name": f"{room} CPU Usage", "device_class": "power_factor", "unit_of_measurement": "%", "state_topic": f"homeassistant/sensor/{room.lower()}/CPU"}
    print(f"Registering sensor: {config}")
    client.publish(f"homeassistant/sensor/{room.lower()}/CPU/config", json.dumps(config))
    config = {"name": f"{room} RAM Usage", "device_class": "power_factor", "unit_of_measurement": "%", "state_topic": f"homeassistant/sensor/{room.lower()}/RAM"}
    print(f"Registering sensor: {config}")
    client.publish(f"homeassistant/sensor/{room.lower()}/RAM/config", json.dumps(config))
    config = {"name": f"{room} Disk Usage", "device_class": "power_factor", "unit_of_measurement": "%", "state_topic": f"homeassistant/sensor/{room.lower()}/Disk"}
    print(f"Registering sensor: {config}")
    client.publish(f"homeassistant/sensor/{room.lower()}/Disk/config", json.dumps(config))

registerSensors()
while True:
    client.publish(f"homeassistant/sensor/{room.lower()}/CPU", psutil.cpu_percent())
    client.publish(f"homeassistant/sensor/{room.lower()}/RAM", psutil.virtual_memory().percent)
    client.publish(f"homeassistant/sensor/{room.lower()}/Disk", psutil.disk_usage('/').percent)
    sleep(5)