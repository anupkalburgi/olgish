- Talk out loud about trade offs
# Concepts
- Distributed Systems
-  Load Balancing
-  Caching
- Consistent hashing
- CAP Theorem
- Data Partitioning
- Indexes
- Proxies
- Replication
- SQL vs NoSQL


## Distributed Systems
- Scalability
- Reliability
- Availability
- Efficient 
- Serviceability or Manageability


### Scalability
- Which can continuously evolve/grow to meet the increasing demand
- scaling without performance loss
- not always, adding more machines (adding distribution) will solve a problem.  eg. If the nature of the problem being solved is transactional  in nature which requires Atomic guarantees
- **Types**
	- Horizontal
		- adding more machines
		- the upper bound of how many machines we can add it relatively higher 
		- Generally we can do this with no down time
		- Cassandra and MongoDB provides a easy way to scale by adding in more machines.
	- Vertical
		- adding bigger machines with more RAM and more cores etc
		- there is generally an upper bound to do this, and generally there is down time associated with this
		- MySQL is good example where we can add bigger machine and get a good performance.

### Reliability
- Machine are going to fail at some point of time in operation. 
- A distributed system is considered reliable if one of more machines or software component  going down/ failing will not effect the service being rendered. 
	- **Should not loose what the capability of doing the a thing **  like adding to shopping cart and checking the inventory, we can achieve that by having two machines performing the same service
	- **It should not loose data as well**  that means we will have to have multiple copies of the data, and a way to retrieve that eg: in Cassandra we can having multiple nodes storing the piece of data.
- Most of the time this can be achieved by having multiple machines or components that are doing the same thing. 


### Availability (is a number)
-  the amount of time that the system remains operational.
-  is a system is reliable, then it is considered generally available
-  reliable systems does not really mean available, we have to consider even the quality of the service. Eg. A system might be loosing transactions while being available but it is not reliable as it is not doing what it is intended to do.

### Efficiency
- There are two important metrics we can measure
	- **Throughput **
		- How many messages or transactions can a given system process in a second (or a given amount of time)
	- **Latency**
		- How much time does it take to process a transaction or a message 
	- A Note: Always measuring averages might not me a good idea, we might want to look at the histogram, and median

- The other part of efficiency is **cost** which is pretty hard to come up with given all the components of the systems like network costs etc.


### Serviceability and Manageability (Can be part of Efficiency ?)
- How easy is it to operate and maintain
- how easy is it to fix a bug, or replace a faulty part of the machine
	- to do that we need good monitoring systems 
	- logging
	- and recovering from a failed system



## Load Balancing
- Why 
- Algorithms
- Redundant Load Balancers

![Pasted_image_20200926135037](/processed/images/Pasted_image_20200926135037.png)

### Why
- High availability - By removing dependency of on one server
- Better response times and maintaining responsiveness
- can give insights into performance and bottlenecks and can drive business decisions

### Algorithms
Load balancers keep track of server health  and direct the traffic to only the healthy servers. Checks are run using health check end points most of the time.
- **Least Connection Method**: to the server with least active connections. When client need persistent connections eg: chat applications or database applications
- **Least Response Time Method**: to server with least active connections and lowest average response method 
- **Least Bandwidth method**: to servers that is least MB/s usefull for static file server
- **Round Robin**: has a list of severs, and every time a request comes in it is directed to the next server on the list.
- **Weighed Round Robin**: each server has a weight generally representing the capacity, the next server with maximum weight get the request
- **IP Hash**: the IP of the client can be used to has and direct the server, and this can be bad then a single IP source is making a lot of requests .. eg: a single server making 90% of the database calls, one sever can become overloaded


### Redundancy
Generally having once load balancer will make that as a single point of failure. To overcome this we can use a cluster of load balancers.


## Caching
- locality of reference .  
- Exists pretty much every where, cpu, application server, web severs
- CDN - content delivery network
- the idea is, the requested data will most probably be re requested again soon. So we keep that in a fast accessible place. 
- **Challenges ** 
	- ***how to keep it in sync with the data that being updated***
		- ***Write through*** - before writing to secondary storage write to cache, 
			- Data is always upto date, and data loss chances are low
			- downside is if a data is updated too often we will have high write latency
		- ***Write Around cache*** - directly write to the secondary storage. Down side is cache miss rate goes up
		- ***Write-back Cache*** - we write to the cache and then later on propagte the change to secondary storage.
			- downside is we can end up having data loses because of system fails
	- ***How to make sure cache size is in check***
		there are a number of algorithms to do this
		- LRU 
		- FIFO
		- LIFO
		- LFU - least frequently used
		- Random Replacement (RR)