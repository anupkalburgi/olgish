# Complexity Analysis
Helpful Resources 
- [https://www.youtube.com/watch?v=JzjkWMTPkdA]( Introduction and motivation - YouTube) 
- [https://www.youtube.com/watch?v=Q0pWMzPAdYM]( Input size, worst case, average case - YouTube)  
	Gives very good intuition of what is complexity, and how the numbers matter

## Topics
- Complexity
	- Proof by Inductions
		- Prove for trivial value like 0,1,2, and assume the answer to be right till n-1, then prove the answer to be correct for n+1. That is in nut shell recursion


### Day 1
- Why do computers take time do anything 
- Why do we care that it actually takes time
- Now that we know we care about why computers take time, we need a way of measuring how long they take, how do we measure them


### Day 2 - Tuesday
- How to measure growth
- what is the way to prove it

####  Insertion Sort 
Code in python-code dir
- Worst case - when the whole list if reversed
	- [100 Steps](http://pythontutor.com/visualize.html#code=def%20insertion_sort%28elms%29%3A%0A%20%20%20%20n%20%3D%20len%28elms%29%0A%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20j%20%3D%20i%0A%20%20%20%20%20%20%20%20while%20%28j%20%3E%200%20and%20elms%5Bj%5D%20%3C%20elms%5Bj-1%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20tmp%20%3D%20elms%5Bj-1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20elms%5Bj-1%5D%20%3D%20elms%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20elms%5Bj%5D%20%3D%20tmp%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20j%20-%201%0A%20%20%20%20return%20elms%0A%0Ainsertion_sort%28%5B6,5,4,3,2,1%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
- Average Case - when some elements are reversed
	- [70 Steps](http://pythontutor.com/visualize.html#code=def%20insertion_sort%28elms%29%3A%0A%20%20%20%20n%20%3D%20len%28elms%29%0A%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20j%20%3D%20i%0A%20%20%20%20%20%20%20%20while%20%28j%20%3E%200%20and%20elms%5Bj%5D%20%3C%20elms%5Bj-1%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20tmp%20%3D%20elms%5Bj-1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20elms%5Bj-1%5D%20%3D%20elms%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20elms%5Bj%5D%20%3D%20tmp%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20j%20-%201%0A%20%20%20%20return%20elms%0A%0Ainsertion_sort%28%5B5,4,3,1,2,6%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
- Best case - when the elements are reversed
	-  [25 Steps](http://pythontutor.com/visualize.html#code=def%20insertion_sort%28elms%29%3A%0A%20%20%20%20n%20%3D%20len%28elms%29%0A%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20j%20%3D%20i%0A%20%20%20%20%20%20%20%20while%20%28j%20%3E%200%20and%20elms%5Bj%5D%20%3C%20elms%5Bj-1%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20tmp%20%3D%20elms%5Bj-1%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20elms%5Bj-1%5D%20%3D%20elms%5Bj%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20elms%5Bj%5D%20%3D%20tmp%0A%20%20%20%20%20%20%20%20%20%20%20%20j%20%3D%20j%20-%201%0A%20%20%20%20return%20elms%0A%0Ainsertion_sort%28%5B1,2,3,4,5,6%5D%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)


- Big-Oh notation #important #understand
	- It is all about how the growth is
- amortized complexity

##### Memory Organization in Computer
![[Pasted image 1.png]]

#### Complexities 
- Linear -- O(n)
- Quadratic -- O(n2)
- Cubic -- O(n3)
- Logarithmic -- O(log n)
- Exponential -- O(2n)
- Square root -- O(sqrt n)
![[Pasted image 2.png]]
(source: http://science.slc.edu/~jmarshall/courses/2002/spring/cs50/BigO/index.html)
Idea to communicate, how we use number of times something is called as a proxy for time




Euclid algorithms from AoCP


Step
- Basic Operation 
- assigning a value
- a < b 
- we can define our steps with as block

What is the time taken proprtional to 
- n i.e the input size
- worst possible case


Show analysis of algorithms 
- O(n2)
- selection sort

log (2) 1000 = 10


#### Day3 - Examples

#### Day 4/ 5 Problems