import time
import paho.mqtt.client as mqtt_client
import requests
import logging
import platform

broker = "broker.emqx.io"
user_service_url = "http://localhost:8000/register"

logger = logging.getLogger('subscriber')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('subscriber.log')
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

common_file_handler = logging.FileHandler('common.log')
common_file_handler.setLevel(logging.DEBUG)
common_file_handler.setFormatter(formatter)
logger.addHandler(common_file_handler)


def register_user():
    response = requests.get(user_service_url)
    user_id = response.json()["user_id"]
    return user_id

def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    logger.debug(f"Received message: {data}")
    print("received message =", data)

def main():
    client_id = register_user()
    client = mqtt_client.Client(client_id)
    client.on_message = on_message

    logger.info(f"Running on {platform.node()}")
    print("Connecting to broker", broker)
    logger.debug("Connecting to broker")
    client.connect(broker)
    logger.debug("Connected to broker")
    client.loop_start()
    logger.debug("Loop started")
    print("Subscribing")
    logger.info("Started subscribing")
    client.subscribe("lab/leds/state")
    while True:
        time.sleep(1000)
    client.disconnect()
    client.loop_stop()
    logger.debug("Disconnected from broker")

if __name__ == "__main__":
    main()