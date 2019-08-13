import socket
import time
import datetime
import os
import shutil

frequency = 100  # set frequency
path = "./results/"  # set file path


def main(args=None):
    ip_port = ('192.168.1.2', 9999)
    # ip_port = ('127.0.0.1', 9999)
    BUFSIZE = 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for y in range(1, 4):

        print("start " + str(y) + " times!")
        f = open(str(frequency)+"_ros2.csv", "w+")
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
            # print('message id is : "%s", massage latency: is "%s"  ms' % (str(data, 'utf-8'), message_latency))

            f.write(msg + "," + str(message_latency) + "\n")
            time.sleep(1/frequency)

        f.close()
        print("finish " + str(y) + " times!")
        shutil.move(str(frequency)+"_ros2.csv", path+str(y))
        time.sleep(1)

    client.close()


if __name__ == '__main__':
    # Runs a talker node when this script is run directly (not through an entrypoint)
    main()
