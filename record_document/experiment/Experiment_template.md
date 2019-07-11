# Experiment 1: Robot crash/Network failure during offloading 

## Objective
What do you want to check/analyse?
To see how the AMP-like offloading deals with failure. In particular, how it reacts when there are robot crashes in the team of robots, or when some/all of the robots lose their network connection.

## Rationale
Why do you need this experiment?
Multi-robot systems are prone to failure. Therefore, when we are performing computational offload in such systems, it is important to be able to deal with failures. In particular, robot crashes and network failures are two common types of failures that we should be able to deal with. 
 
## Procedure
How will you run the experiment?
5 Raspberry Pis running Route Planning Server.

A single robot needs to calculate 10 routes. The AMP-like autonomous client decides where the tasks should run and sends them to the appointed robots. 

When the tasks are offloaded failures are introduced to the system. They are two types:
•	(1,2,3,4) robots are shut down.
•	(1,2,3,4) robots lose network connection.

We record the time to complete the tasks and the allocation of tasks on robots before and after the failures occur.

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

