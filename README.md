### Software-Defined Concurrency Control of Job/Task Performance Optimization in Hadoop

The goal of this project is to design a software-defined feedback controller that can dynamically tune the configurable parameters of a Hadoop Cluster based on the resource utilized which is taken from the measured output.

This controller was tested on a 3-node HADOOP cluster. (1 master and 2 slave nodes)

The "Global Controller" module was implemented in the master node to monitor the resource usage in the cluster and control the resources allocated to the nodes.

The "Local Controller" module was implemented in the slave nodes to monitor the resource usage and transfer the information to the master node periodically.




