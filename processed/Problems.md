## Problems

### Search a element in the a array, 
[1,2,3,4,5, 15, 35]
15
- we can do a linear scan and get a O(n)
- Binary search will give a O(log n) solution

Idea
Pseudo code
Complexity
Code

###  Find the number of elements that are smaller on the right
eg - 
[3,4,9,2,6,1]
[2,2,3,1,1,0]

This is a interesting problem to carry along
1. Has a brute force O(n^2) algorithm does not need s lot of pre existing alogs -
2. then are easy pit falls 
	1. we can try sort it but we will loose information
	2. Teaches that we can start from end of the array to solve a problem
	3. the there is binary search that can be emulated


###  Longest Increasing Subsequence 
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

- Easy O(n^2) Solution
- But there is a dynamic solution which is also O(n^2)
- And then there is a solution using binary search and Dynamic programming


Greedy Algo counters example, where the input is all the same tie