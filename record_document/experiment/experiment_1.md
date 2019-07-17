# Experiment 1: Revising wifi router performance experiment

## Objective
This experiment investigates the performance in different frequency of message passing by using Wi-Fi network connection in a router. In order to acquire a detailed understanding of the performance characteristics of ROS’ communication channels, this experiment use two ROS hosts to commnunicate with each other and get the message latency results in different frequency.
## Rationale
A prior investigator, Issac, had begun investigation of building such experimental environment. To understand project and make further project, I reproduced his experiment and get result which is a bit different with him. This experiment provides familiarity with ROS and grasp an understanding of how ROS communication works.
## Procedure


## Hardware Configuration
Raspberry Pi 3B
A router
A control computer

## Software Configuration
Ubuntu
ROS Kinetic 
network configuration for all LAN devices

## Hypothesis
What do you expect?
•	Robot crashes and network failures should not prevent the tasks to be eventually executed successfully
•	Robots shutdown and robots losing network connection should have the same impacteffect on the system. (From the point of view of the amp it is the same failure)
•	When robots fail, the AMPs that are running on these robots, should be resentmigrated to other robots in the system. The way the AMPs are allocated after the failure should lead to fairly evenly load distribution.
 
## Results and Observations
Explicitly say what you have observed
## Conclusion

