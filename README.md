Goal:
Design a Software-defined controller for performance optimization in HADOOP 

Implementation:
Designed a software-defined controller based on a correlation obtained from the cluster’s resource usage pattern that improved the concurrency of MR jobs by 83%.
This controller was tested on a 3-node HADOOP cluster. (1 master and 2 slave nodes)

The "Global Controller" module was implemented in the master node to monitor the resource usage in the cluster and control the resources allocated to the nodes.

The "Local Controller" module was implemented in the slave nodes to monitor the resource usage and transfer the information to the master node periodically.



