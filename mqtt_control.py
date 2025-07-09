import paho.mqtt.client as mqtt

def send_mqtt_command(location, device, action):
    topic = f"home/{location}/{device}"
    client = mqtt.Client()
    client.connect("broker.hivemq.com", 1883, 60)
    client.publish(topic, action)
    client.disconnect()
    return f"Command sent: {topic} → {action}"