from zmqpubsub.zmq_subscriber import Subscriber


def callbackFunc(message_in_json_object):
    print(message_in_json_object)
    print("")


if __name__ == '__main__':
    #  IMEC public IP: 193.190.127.147, for testing local host IP: 127.0.0.1
    subscriber = Subscriber(ip='193.190.127.147', port='2004')
    subscriber.subscribe(topic="allData", callback=callbackFunc)
