# 1-distributed_web_infrastructure
![simple web stack](https://github.com/MohamedElAllouli/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.JPG)

## Description 
This is a distributed web infrastructure that tries to reduce  traffic to the main server by distributing some of the load to a replica server using a load balancing server  between the two machines master (primary and replica). 
## Details about this infrastructure 
* The distributed algorithm on which the load balancer is configured  and how it works.  The HAProxy load balancer is configured using the *Round Robin* distribution algorithm.
 This algorithm works by using each server behind the load balancer in turn, based on their weight. This is also probably the smoothest and fairest algorithm because server processing time is still evenly distributed.As a dynamic algorithm, allows server weights to be adjusted at any time.
* Configuration enabled by load balancer.  HAProxy load balancer allows "Active-Passive" configuration instead of "Active-Active" configuration. In an "Active-Active" configuration, the load balancer distributes the workload across all nodes  to prevent overload of a single node.
 Because there are more nodes available to serve,  throughput and response times will also improve significantly.
 On the other hand, in an Active-Passive configuration, not all nodes are  active (can receive workload at any time).
 For example, in the case of two buttons, if the first button is  active, the second button must be passive or in standby mode.
 The second or subsequent passive node can become the active node if the previous node is inactive.
* How the "Primary-Replica" ("Master-Slave") database cluster works. The "Master Replica" configuration configures one server to act as the "Primary" server and the other server to act as a "Replica" of the "Primary" server.
 However, the "Master" server is capable of making read/write requests while the *Replica* server is only capable of making read requests.
 Data is synchronized between the Primary and Replica servers every time the *Primary* server performs a write operation.
* Difference between Master node and Clone node for an application.
 The Master node is responsible for all  write operations requested by the site while the Replica node can handle read operations, which reduces read traffic to the Master node.
## Problems with this infrastructure 
* There are multiple SPOFs (Single Point Of Failure).
 For example, if the main MySQL database server is down, the entire site will not be able to make changes to the site (including adding or removing users).
 The server that contains the load balancer and  application server that connects to the main database server is also a SPOF.
* Security issue.
 Data transmitted over the network is not encrypted with an SSL certificate so that hackers can spy on the network.
 There is no way to block unauthorized IP addresses as there are no firewalls installed on any of the servers.
* Unattended.
 We have no way of knowing the status of each server because they are not  monitored.
Rephrase

 

