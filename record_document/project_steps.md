[TOC]

## Ubuntu and ROS system installation
1. Down load the latest version image of Ubuntu with ROS in the ROS official website.
2. Write the image to Raspberry Pi directly.
3. Now the ubuntu system with installed ROS and envoriment 
4. Type `roscore` to test whether ROS system exist.

### Issues
Raspbian latest system(buster) is not well supported by ROS system. Therefore, there are many bugs and manually installation steps to solve when you want to install ROS in Raspbian operating system. Then the ubuntu is recommend system as official website said.

## Router network configuration
1. Each Pi connect to the LAN in one router.
2. Assign static IP address to each Pi for ssh remote control.
3. Using one computer to join this LAN for controlling the different Pi.
4. `ssh ubuntu@{ip address}` with password.

## Communication between different ROS hosts
 each host configuration file list should be as below:
    `sudo vim /etc/hosts`
    modify /etc/hosts file of your machine. Each ip address respond to one hostname which you give.
    Example hosts file:
 
    ```
	::1     ip6-localhost ip6-loopback
	fe00::0 ip6-localnet
	ff00::0 ip6-mcastprefix
	ff02::1 ip6-allnodes
	ff02::2 ip6-allrouters

	192.168.1.11 com1
	192.168.1.12 com2
    ```
    
###  1. Check communication status
enter ROS system in every ubuntu system
On com1:
`ssh com1 `
`ping com1`
`ping com2`
On com2
`ssh com2`
`ping com1`
`ping com2`
If ping successfully and you can go to the next step or you should check the router network.
### 2. Multiple hosts configuration
#### Start the listener
`cd ~/catkin_ws`
`touch config_ip.sh` creat auto executable file
`vim config_ip.sh` 
The host name and ip address is respond to each Raspberry Pi, but the Master URI should be identical.

```
# /bin/sh
export ROS_HOSTNAME=com1
export ROS_IP=192.168.1.11
export ROS_MASTER_URI=http://com1:11311/
```

`source config_ip.sh` execute this file to execute all command inside it.

Then run the listener file:
`cd ~/catkin_ws`
`source ./devel/setup.bash`
`rosrun rospy_tutorials listener.py`

#### Start Talker
File configuration is same steps with the listener. 
Run the talker file:
`cd ~/catkin_ws`
`source ./devel/setup.bash`
`rosrun rospy_tutorials talker.py`

When listener can receive message from talker, communication successful.
### 3. Issues
Make sure you set the ROS hostname and IP address correctly and you must explicitly set it. **Otherwise the listener cannot receive talker because the host cannot find it in the network.**
You can check the hostname and ip address setting: 
`echo $ROS_HOSTNAME`
`echo $ROS_IP`

## Test Message latency
Use scp copy file and folder to remote Pi.

install catkin
`cd /home/ubuntu/catkin_ws`
`catkin_make install`

lisetener:
`cd /home/ubuntu/catkin_ws/src/rosberry_experiments/src`
`chmod +x test_latency_echo.py`
`rosrun rosberry_experiments test_latency_echo.py`

sender:
`cd /home/ubuntu/catkin_ws/src/rosberry_experiments/src`
`chmod +x test_latency_main.py`
`source run_experiment.sh`

Wait until the script running on the main robot exits and then Ctrl+C the script on the other robot if no longer needed (it will otherwise continue listening for messages and passing them back at the set rate).
The result will store in the result folder then you can process the data.