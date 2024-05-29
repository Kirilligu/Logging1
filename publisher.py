import time
import paho.mqtt.client as mqtt_client
import random
import requests
import logging
import platform

broker = "broker.emqx.io"
user_service_url = "http://localhost:8000/register"

logger = logging.getLogger('publisher')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('publisher.log')
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

def main():
    client_id = register_user()
    client = mqtt_client.Client(client_id)

    logger.info(f"Running on {platform.node()}")

    print("Connecting to broker", broker)
    logger.debug("Connecting to broker")
    print(client.connect(broker))
    logger.debug("Connected to broker")
    client.loop_start()
    logger.debug("Loop started")
    print("Publishing")
    logger.info("Started publishing")

    for i in range(10):
        state = "on" if random.randint(0, 1) == 0 else "off"
        state = state + "ArtemV"
        logger.debug(f"Published message: {state}")
        print(f"State is {state}")
        client.publish("lab/leds/state", state)
        time.sleep(2)

    client.disconnect()
    client.loop_stop()
    logger.debug("Disconnected from broker")

if __name__ == "__main__":
    main()