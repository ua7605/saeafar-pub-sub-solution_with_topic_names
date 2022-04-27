import zmq

if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    socket.bind("tcp://193.190.127.147:9002")  # notice

    while True:
        data = socket.recv_json()
        print('second subscriber: ', data)
        print('\n')