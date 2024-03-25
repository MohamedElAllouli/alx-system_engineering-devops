# 2. Secured and monitored web infrastructure
![Secured and monitored web infrastructure](https://github.com/MohamedElAllouli/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.JPG)
## Description 
In our enhanced infrastructure, we have increased security and monitoring capabilities with the addition of three firewalls, ensuring better protection against unauthorized access. Additionally, by implementing an SSL certificate, we enabled HTTPS encryption for www.foobar.com, improving data security during transmission.
To stay on top of system health and performance, we've integrated three monitoring applications, facilitating data collection for services like Sumo Logic, enabling proactive monitoring and Quickly detect any abnormalities or problems.
## Added items 
### Firewall: We are adding a firewall to improve security by controlling incoming and outgoing network traffic, protecting against unauthorized access and threats hidden network.
### SSL Certificate:  
SSL certificate deployed to enable HTTPS encryption for www.foobar.com, ensuring secure communication between the server and the user's browser, protecting data sensitive  from being intercepted or tampered with.
### Monitoring:
 We integrate customer monitoring  to collect data for services like Sumo Logic, improving system health monitoring, anomaly detection and resolution resolve any issues quickly, thereby improving overall performance and reliability.
 ## What is a firewall used for?
 Firewalls are network security devices or software applications designed to monitor and control incoming and outgoing traffic based on predefined security rules.
 They act as a barrier between trusted internal networks and untrusted external networks.
## Why is  traffic served over HTTPS?
 Traffic is served over HTTPS to ensure secure communication between a client (such as a web browser) and a server.
 HTTPS (Hypertext Transfer Protocol Secure) encrypts  data transmitted between  client and server, ensuring confidentiality and integrity.
## What is monitoring  for?
 Monitoring is used to monitor the health, performance, and availability of various components in a system or network.
 This involves collecting and analyzing data from servers, applications, databases, and other infrastructure components to ensure they work as expected.
## How does the monitoring tool collect data?
 Monitoring tools collect data by continuously querying or querying different metrics from the components they are monitoring.
 This process involves sending queries to  target systems or devices and retrieving specific information, such as CPU usage, memory usage, network traffic, disk I/O, metrics performance, application performance, error logs, etc.
## Explain what to do if you want to monitor the QPS of your web server?
 To monitor your web server's QPS, first choose a monitoring tool like Prometheus or Datadog.
 Install the monitoring agent on your web server and configure it to collect QPS metrics.
 Set up alerts to notify you of any unusual traffic spikes.
 View metrics using a monitoring tool dashboard to track QPS over time.
 Analyze data regularly to optimize server performance and ensure it can handle incoming traffic effectively.
## problem 
with this infrastructure  SSL termination at the load balancer  poses a security risk because the decrypted traffic is then transmitted as plain text within the internal network, potentially exposing sensitive information to unauthorized access.
 Having only one MySQL server capable of accepting writes creates a single point of failure (SPOF), as any failure of the MySQL server can lead to downtime and data loss.
 Having servers with all the same components can be a problem because it increases uniformity, leaving the infrastructure vulnerable to widespread failures or security breaches if vulnerabilities affect all versions of a specific component.
 

