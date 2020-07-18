# Recap Basics
## Day 1
####  Programming Laguages 
Generally thinking programming language as a tool we need to solve a problem is good. And how you solve a problem or view a problem can be done in two popular ways
-   Object Oriented Way
	-   java 
	-   python
	-   scheme
-   Functional Way
	-   Haskell
	-   Scala
	-   F#
	-   lisp

Both style of programming languages have there own advantages and disadvantages. And most of the time we can use use Non Functional languages to write functional code, and the other way around. The important thining we have to understand is concepts within each, and not how they implement that. We will be dicussing them as we cross over that

![[Pasted image.png]]

We are going to be using python becasue
1. You know it already to a large extent.
2. very good language to use in a interview. 
3. has a low barrier to entry, compared to other langaugaes
4. Most ML frameworks use python


### Setup computer 
- install [wing ide](https://wingware.com/downloads/wing-personal), it is amazing becasue, 
	- gives immediate access to documentation
	- has a way to look at call stack in a readable way 
	- has more tools to explore
- [using home brew](https://gist.github.com/iexa/2ac761bfd96ab78988b76c030d54a5b8)
- 



####  Task for next 2 days
Read the 1st chapter, what the video about object oriented concepts. The idea is finish as much as possible. Wirte all the code necessary.  
- Read [Python Programming 101](https://link.springer.com/chapter/10.1007/978-3-319-13072-9_1)
- Watch [Object Oriented Concepts](https://www.youtube.com/watch?v=WcTPZjUHpUI&list=PL1DE477438120C9EF&index=31) 



## Day 2
Continue doing what you where doing. We will get on the call if you have doubts.

## Day 3
- Generally start with what did you read ? 
- What is the thing that you did not know, but now you know. 
- What are the concepts that you think are important and like to remember



### Topics to Revisit 
Talk about how these are general concepts and generally applies across all the languages, eg Java,Scala,JS.

Generally these topics are convered in programming language courses, it is its own field of study. Though we don't have to understand the depth of the matter, it is essential we understand what these topics are and how we can use them, and what kind of problems we can solve using them

 - Polymorphism
	 - Example in code how how we are using .draw method. In this case the draw method is considered polymorphic, as it can change behaviour depending upon who calls it
 - Inheritance
	 - generally, we have a hirararcy to it. But we will come back to it as we progress
 - Iterator
	 - it is a general concept found in a many languages
	 - it gives a common way of accessing a list like structure. Here the list is refered to as a container. 
	 - An iterator is an object that has methods that allow you to proccess a collection of items one at a time.
	 - Once you process that it is done, you cannot generally can't go back. You can only move forward.  it is "consumed"
	 - Container can be list, tuple, dictonary. Generally it can be any object (remember there is class behind it implementing methods)
	 - If a class/object implements a iterator, generally you can wite a for loop for it. This kind of provides confidence to wirite code in a more general way 
	 - https://docs.python.org/3/glossary.html#term-iterator 
	 - If you have some time https://www.youtube.com/watch?v=V2PkkMS2Ack
 - accumalator 
	 - you have used it few times already 
	 - 
	 ```python
	 
	 def total(input_list = [1,2,3,4,5])
	 	total_sum = 0
		for element in input_list:
			total_sum = total_sum  + element
	 ```
 
 
 
## Day 4 
 
#### Keywords
- Memory Localtion
- Lookup
- Average Access Time


#### Todo
[] Example Program to demonstrate what is growth rate, ideally would like to have graphs. 
1. linear time 
2. Quadratic
3. exponential time
Idea to communicate, how we use number of times something is called as a proxy for time



Euclid algorithms from AoCP


Objectives 
- Object Oriented Programming
- Classes
- Objects