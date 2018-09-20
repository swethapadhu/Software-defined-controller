
This controller was tested on a 3-node HADOOP cluster. (1 master and 2 slave nodes)

The "Global Controller" module was implemented in python in the master node to monitor the resource usage in the cluster and control the resources allocated to the nodes.

The "Local Controller" module was implemented in python in the slave nodes to monitor the resource usage and transfer the information to the master node periodically.



