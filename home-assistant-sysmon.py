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
    config = {"name": f"{room} CPU Temperature", "device_class": "temperature", "unit_of_measurement": "°C", "state_topic": f"homeassistant/sensor/{room.lower()}/CPUTemp"}
    print(f"Registering sensor: {config}")
    client.publish(f"homeassistant/sensor/{room.lower()}/CPUTemp/config", json.dumps(config))

registerSensors()
while True:
    temps = psutil.sensors_temperatures()
    cpuTemp = 0
    for name, entries in temps.items():
        if name == 'cpu_thermal':
            for entry in entries:
                cpuTemp = entry.current
    data = {
            'CPU':psutil.cpu_percent(),
            'RAM':psutil.virtual_memory().percent,
            'Disk':psutil.disk_usage('/').percent,
            'CPUTemp':cpuTemp,
           }
    print(data)
    client.publish(f"homeassistant/sensor/{room.lower()}/CPU", data['CPU'])
    client.publish(f"homeassistant/sensor/{room.lower()}/RAM", data['RAM'])
    client.publish(f"homeassistant/sensor/{room.lower()}/Disk", data['Disk'])
    client.publish(f"homeassistant/sensor/{room.lower()}/CPUTemp", data['CPUTemp'])
    sleep(5)