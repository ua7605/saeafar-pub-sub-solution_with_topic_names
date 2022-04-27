import zmq
import time


def create_pub_socket():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    #socket.connect("tcp://193.190.127.147:9002")
    socket.connect("tcp://127.0.0.1:9002")
    return socket


def publish(pub_socket):
    message = {
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

    pub_socket.send_json(message, 0)
    return message


if __name__ == '__main__':
    socket = create_pub_socket()

    while True:
        print('\n')
        print('publisher: ', publish(socket))
        time.sleep(1)
