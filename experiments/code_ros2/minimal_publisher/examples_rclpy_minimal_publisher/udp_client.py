import socket
import time
import datetime


def main(args=None):
    ip_port = ('192.168.1.2', 9999)
    BUFSIZE = 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for x in range(1000):
        msg = str(x)
        time_before = datetime.datetime.now().strftime('%H:%M:%S.%f')
        print('message send "%s", time is "%s"' % (x, time_before))
        client.sendto(msg.encode(), ip_port)

        data, server_addr = client.recvfrom(BUFSIZE)
        time_after = datetime.datetime.now().strftime('%H:%M:%S.%f')
        print('message receive "%s", time is "%s"' %
              (str(data, 'utf-8'), time_after))
        time.sleep(1)

    client.close()


if __name__ == '__main__':
    # Runs a talker node when this script is run directly (not through an entrypoint)
    main()
