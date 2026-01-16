from paho.mqtt import client as mqtt_client
import random
import time
import json

BROKER = 'broker.emqx.io'
PORT   = 1883
TOPIC  = "device_linux/publish/anhtdh"
CLIENT_ID = "anhtdh@viettel.com.vn"

# Callback function for connecting the broker --> after client connected successfully -> rc parameter
def connect_mqtt():
    def on_connect_callback(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected successfully to broker!")
        else:
            print("Failed to connect to MQTT broker, return code %d\n", rc)
        
    client =  mqtt_client.Client(client_id=CLIENT_ID, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect_callback
    client.connect(BROKER, PORT)
    return client


def mqtt_publish_to_broker(client):
    msg = json.dumps({"Name" : "TranDucHoangAnh", "email" : "anhtdh@viettel.com.vn", "Job" : "Embedded"})
    res = client.publish(TOPIC, msg)
    status = res[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{TOPIC}`")
    
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(TOPIC)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    mqtt_publish_to_broker(client)
    client.loop_stop()


if __name__ == '__main__':
    run()