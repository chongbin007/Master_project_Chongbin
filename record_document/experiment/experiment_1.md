# Experiment 1: Robot crash/Network failure during offloading 

## Objective
What do you want to check/analyse?
To see how the AMP-like offloading deals with failure. In particular, how it reacts when there are robot crashes in the team of robots, or when some/all of the robots lose their network connection.

## Rationale
Why do you need this experiment?
Multi-robot systems are prone to failure. Therefore, when we are performing computational offload in such systems, it is important to be able to deal with failures. In particular, robot crashes and network failures are two common types of failures that we should be able to deal with. 
 
## Procedure
Steps needed to run message latency experiments under ROS for a pair of robots:

1. Connect all raspberry pi into one LAN network.

2. 用ip地址来确定每个ros.Associate the IP addresses of each robot with a hostname, by modifying the /etc/hosts file of your machine. The IP addresses are labelled on each robot. Alternatively, just use the IP addresses directly. Example hosts file:

3. 启动。Boot up robots. They need maybe 30 or so seconds to start up once you put in the batteries.

4. ssh远程登录多个板子。Using separate terminals, ssh into the robot pair you want to use in the experiment, by logging in as user pi with password "raspberry". Example:
	ssh pi@masterpi
	ssh pi@mercurypi

5. 进入ROS工作区。Navigate to the main ROS workspace on each robot:

	`cd ~/catkin_ws/`

6. Choose which robot will set the timestamps and record the measurements and which robot will simply ping back the messages. On the measurement robot, make sure the script test_latency_main.py exists. On the pingback robot, make sure the script test_latency_echo.py exists. These scripts can be found in the repository, under:
	/al-internship/ROSberry_Experiments/rosberry_experiments/src/Line_Formation/Experiments/Scalability/NetworkTraffic

7. Choose one of the robots to host the master (if not using a seprate master), open a separate ssh terminal to it and run:
	
		roscore

	This will start the ROS master service.

8. If you started a master on one of the experiment robots like in step 4, then, on the other robot, run:
	
	export ROS_MASTER_URI=http://**name_of_master**:11311/

	**name_of_master** should be replaced with the hostname of the machine on which you ran "roscore" (e.g. masterpi). This will tell the other robot where to find the master.

9. Going back to your initial robot terminals, on the pingback/echo robot run:
	
	rosrun rosberry_experiment test_latency_echo.py 10 1000
	
	Then, on the main robot, run:

	rosrun rosberry_experiments test_latency_main.py 10 1000

	10 in this case represents the publishing rate for the messages. It should be identical for both scripts, to ensure the pingback/echo robot sends the messages back no faster (and no slower) than the main robot sends them.

	1000 is the number of messages to be sent over the network.

10. Wait until the script running on the main robot exits and then Ctrl+C the script on the other robot if no longer needed (it will otherwise continue listening for messages and passing them back at the set rate).

11. Run "ls" on the main robot. There should now be a file titled times_RATE.txt, where RATE is the set publishing rate. This contains N lines - corresponding to each of the N messages -, where each line is composed of:
 
	ID(int),SendTime(float),RecvTime(float)

	SendTime and RecvTime are Unix time values and thus represent the seconds (+fractions of a second to a two-decimal precision) that have passed since the start of the Unix epoch.

Notes:
	* Make sure you save or copy the times_RATE.txt files before re-running the experiment with the same rate value, as the old values will be overwritten.
	* You can copy over files from the robots to your machine by opening a terminal on your machine and running scp, like in the example:

		scp pi@masterpi:/home/pi/ros_catkin_ws/src/rosberry_experiments/src/times_3.txt ./

	* The main script will by default sleep for 5 seconds after the last message was sent and only then exit, to make sure the subscriber (which runs in a separate thread) has more than enough time to receive any messages that are still inbound.

## Hardware Configuration
Raspberry Pi 3
SunFounder robots on batteries?
Connection? 
 
## Software Configuration
Ubuntu
Ros Kinetic 1.12.12
 
## Hypothesis
What do you expect?
•	Robot crashes and network failures should not prevent the tasks to be eventually executed successfully
•	Robots shutdown and robots losing network connection should have the same impacteffect on the system. (From the point of view of the amp it is the same failure)
•	When robots fail, the AMPs that are running on these robots, should be resentmigrated to other robots in the system. The way the AMPs are allocated after the failure should lead to fairly evenly load distribution.
 
## Results and Observations
Explicitly say what you have observed
## Conclusion

