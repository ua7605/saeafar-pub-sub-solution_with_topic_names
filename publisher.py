import json
import time

from zmqpubsub.zmq_publisher import Publisher

if __name__ == '__main__':
    topic: str = "allData"

    # Creating the publisher. # IMEC public IP: 193.190.127.147
    publisher = Publisher(ip='127.0.0.1', port='2004')
    # publisher.start()

    # Seafar JSON object data
    seafar_data_set = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                4.85,
                51.06
            ]
        },
        "properties": {
            "sogKph": 34.5,
            "headingTrueDegrees": 156.9,
            "epochSeconds": 1643640902.7957883
        }
    }

    # To create a string of a JSON object representing the contents of 'example_data_set'
    seafar_data_json_object = json.dumps(seafar_data_set)

    while True:
        time.sleep(1)
        publisher.publisher_zmq.publish(topic="allData", payload=seafar_data_json_object)
        print("server published on topic: " + topic + " the following data : " + seafar_data_json_object)
