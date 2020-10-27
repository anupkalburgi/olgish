database design 
OOO Design 
API design 

System API Design Questions

## Generating Phone Numbers 
```
You are supposed to design an API and a backend for a system that can allot phone numbers to people living in a city. The phone numbers will start from 111-111-1111 and end at 999-999-9999. The API should enable the clients (people in the city) to do the following:

When a client requests for a phone number, it allots one of the available numbers to them.

Some clients may want fancy numbers, so they can specifically ask for a number to be alloted to them. If the requested number is available then the system allots it to them, otherwise the system allots any available number.

The system need not have to know which number is alloted to which client. The same client may make successive requests and get multiple phone numbers for himself, but the system is not bothered. At any point of time, the system only knows which phone numbers are alloted and which phone numbers are free
```

Pre Generate all the numbers from 111-111-1111  to 999-999-9999 may be in a sql table called

phone_number_available
phone_number_inuse 

there is downside to this in terms of searching if a number is available to use, to over come that we can use something like binary search to speed the search_up 


get_phone_number() -> Either[Success, Fail] 
	get_next_number() 
		could take from the available table and move them to in_use table that way the request is served fast
		and we are also keeping track of the used number 

get_fancy_number(requested_number): Either[Success, Fail] -> 
	could do the same thing as the above but this time can do check. using the available table and if not can return an error.
	
	
was not asked in the questions we might want to also design an API that can give up a phone number 
that way it can be deleted from the inuse database and moved to available table 


## Design Search Typeahead
- again this is one if the frequently asked questions 
- and somewhat not very straight forward
	- we can use trie like structure and get away to a very last extent 
![[Pasted image 20201018173024.png]]

- Things that I did not think about 
	- Like how would i get only the top 10 of suggestions - computing that very request is very expensive and to overcome that we can just store the suggestions at the node and probably that is ok to take more memory 
	- and updating the tire is very expensive to do that we can have map reduce jobs to do it a fixed intervals 
	- another important this is about how we are doing to store this tree like structure we might have to serialization and deserialization - and we create filed that can store the tree level by level and thus can construct quickly 


## API Rate Limiter
- what should the api looks like 
- we should serve only limited number of requests per second
	- and that limitation can be on device IP and such 
	- in this case let us assume it is going to be based on the device
- Limit the number of requests an entity can send to an API within a time window, e.g., 15 requests per second.
- The APIs are accessible through a cluster, so the rate limit should be considered across different servers. The user should get an error message whenever the defined threshold is crossed within a single server or across a combination of servers.
- ![[Pasted image 20201018175624.png]]
- Things that I did not consider about 
	- did not worry about what the memory requirements are going to be like
	- and there a alternative implementation, where we can pre divide a times and then use that as fixed buckets and the each bucket having a counter and if the counter at at any given slot goes beyond the limit we can stop the request 	
	- actually both the algorithms that are described in educative are sliding window and i did not understand it properly 