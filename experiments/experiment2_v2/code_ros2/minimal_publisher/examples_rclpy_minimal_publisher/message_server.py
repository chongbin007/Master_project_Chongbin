import socket


def main(args=None):
    BUFSIZE = 1024
    # server address
    ip_port = ('192.168.1.2', 9999)
    # ip_port = ('127.0.0.1', 9999)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #
    server.bind(ip_port)

    print("server start!!!")
    while True:
        # receive data
        data, client_addr = server.recvfrom(BUFSIZE)
        #print('server receive data: ', data)

        server.sendto(data, client_addr)

    server.close()


if __name__ == '__main__':
    # Runs a talker node when this script is run directly (not through an entrypoint)
    main()
