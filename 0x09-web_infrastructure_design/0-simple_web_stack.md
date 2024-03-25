# 0. Simple web stack
![simple web stack](https://github.com/MohamedElAllouli/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.JPG)

## Description: 
This web infrastructure consists of a server with Nginx as the web server that handles HTTP requests. In addition to application code files, it also contains an application server that executes application logic. MySQL databases store and manage data for your applications. The domain name foobar.com consists of a www record pointing to the server's IP address 8.8.8.8 However, this setup can face challenges such as single points of failure, downtime during maintenance, and limited scaling to handle high traffic.
## What is a server?
 A server is a computer program or hardware device that provides functionality or services to other computers or users in a network.
## What do domain names ?
 Domain names provide easy-to-remember names for sites on the Internet, such as websites and email servers,  instead of complex numerical IP addresses.
 It's about providing a user-friendly way to access resources.
## What type of DNS record is the www  in www.foobar.com?
 The "www" in the domain name "www.foobar.com" is typically an A record that maps the domain name to his IPv4 address (address record).
## What  role does a web server play?
 The role of a web server is to process HTTP requests from clients (such as web browsers) and send back web pages or other resources requested by the client.is to respond with.
## What is the role of an application server?
 The role of an application server is to provide client applications with access to business logic and application functionality.
## What role does the database play?
 The role of a database is to store, organize, manage, and retrieve structured information or data. It provides a structured format for storing data and allows users to easily access, modify, and manage the data according to their needs.
## What does the server use to communicate with the computer of the user requesting the website?
 The server uses Hypertext Transfer Protocol (HTTP) to communicate with the user's computer  requesting the website.
 communicate with the user's computer.
# The issues with this infrastructure: 
## SPOF 
Single Point of Failure (SPOF): The infrastructure has a single server that  fails for any reason (hardware failure, software crash, etc.) means that it occurs. ).  Your entire system will fail and your website will experience downtime.
## Downtime when maintenance is required Downtime during maintenance: When maintenance is required.
 For example, if you deploy new code that requires restarting your web server (Nginx), your website will experience downtime during the restart process.
 This can cause inconvenience to  users and  loss of business.
## Unable to scale with too much incoming traffic.
 With just one  server and one application server for him, the infrastructure cannot easily scale to handle the large amount of incoming traffic. Increased traffic can overload the server, causing poor performance or  crashes.

