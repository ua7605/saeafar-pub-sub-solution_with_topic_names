import zmq
import threading


class Subscriber:
    def __init__(self, ip, port):
        self.subscriber = ZMQSubscriber(ip, port)

    def subscribe(self, topic, callback):
        self.subscriber.subscribe(topic, callback)


class ZMQSubscriber:
    def __init__(self, ip, port):
        self.callback = None
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.bind = 'tcp://' + ip + ':' + port

    def subscribe(self, channel, callback):
        self.socket.bind(self.bind)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, channel)
        worker = threading.Thread(target=self.fetch_updates)
        worker.start()
        self.callback = callback
