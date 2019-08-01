import socket
import time
import datetime


def main(args=None):
    # ip_port = ('192.168.1.2', 9999)
    ip_port = ('127.0.0.1', 9999)
    BUFSIZE = 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    f = open("ros2_latency.csv", "w+")
    f.write("id" + "," + "message_latency" + "\n")
    for x in range(1000):
        msg = str(x)
        # time_before = datetime.datetime.now().strftime('%H:%M:%S.%f')
        time_before = datetime.datetime.now()

        #print('message send "%s", time is "%s"' % (x, time_before))
        client.sendto(msg.encode(), ip_port)

        data, server_addr = client.recvfrom(BUFSIZE)
        # time_after = datetime.datetime.now().strftime('%H:%M:%S.%f')
        time_after = datetime.datetime.now()

        #print('message send "%s", time is "%s"' % (x, time_after))

        message_latency = (time_after - time_before).total_seconds() * 1000
        print('message id is : "%s", massage latency: is "%s"  ms' %
              (str(data, 'utf-8'), message_latency))
        f.write(msg + "," + str(message_latency) + "\n")
        time.sleep(0.05)
    f.close()
    client.close()


if __name__ == '__main__':
    # Runs a talker node when this script is run directly (not through an entrypoint)
    main()
