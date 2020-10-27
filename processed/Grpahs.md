- List of problems 
	- has very nice breakdown of problems one should be doing in graphs
	- https://leetcode.com/discuss/general-discussion/655708/Graph-For-Beginners-Problems-or-Pattern-or-Sample-Solutions

I will have to at some point of  time I will have to read about probability from the book mathematics for computer science by lee https://courses.csail.mit.edu/6.042/spring17/mcs.pdf
- Feels like I should be knowing this and I feel like it will make me a better computer programmer and generally a better thinker


G = (V,E)
 here the V - vertices and E - Edges - I have never seen this representation being very useful but may be this is useful when analyzing a algorithms and not otherwise 
 Directed Graphs 
 Undirected graph
 
 Topological sorting is very much a graph algorithm though that is not necessaryly a graph problem
 - this has good a very good application in dependency tracking. Like if there is problem like you have to finish a task before you can start another one, topological sorting become very handy 
 - Time analysis of graph algorithms are measured input size and in case of graphs that has to be described in terms of node/vertices and number of edges []
 

## Graphs
- Graph representations 
	- Matrix
	- Adjacency List
	- Trees 
		- the one with parent information 
		- the one with out.. like in case of binary trees

Applications
1. task dependency 
2. search applications 
3. Shortest Path algorithms 
	1. Dijkastras Algorithm - can be implemented with heap to make it linear time 
	2. 
- BFS
	- Algorithms
	- implementations 
	- Shortest path of something
- DFS
	- Algorithm
	- implementation
	- longest possible path
- Union Find
- Are almost all problems based on of matrix or are these some that use python objects with pointers
- Finding cycled
- Dependency
- Topological Sorting - Dependency management	


Learning check point - in any connected graph what is the minimum number of edges possible

- this is very good example to think about. As it forces you to draw various diagram and thing about the problem



Day-1
- Test our understanding, if there is graph  G = (G,V) , what are the maximum number of edges possible
	- this kind of understanding is necessary as this will help us think about the complexity and how to derive the complexity 
- most of the algorithms in graphs are linear time i.e they grow according to the size of the input

			
```
input G = (V,E) // vertices and edges
and if the graph is connected
how many minimum edges are there 
and how many maximum edges are possible
```


BFS
### implement BFS using queue
### length of shortest path with all the other vertices in linear time 
### in linear time how to compute connected components using bfs in a un-directed graph

DFS - probably how one would explore a graph - we  keep going and backtracking only when necessary 
### implementing DFS using recursion and the using explicit recursion
### topological ordering of vertices key technique task scheduling like problems 
### strongly connected components in a graph with application in web 