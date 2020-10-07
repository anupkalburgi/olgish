
1. Problems 
	1. Computer the lowest common ancestor in Binary Tree	- https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ ✅
	2. Is the binary tree balanced - https://leetcode.com/problems/balanced-binary-tree/ ✅
	3. Path Sum - https://leetcode.com/problems/path-sum/ ✅
	4. Maximum depth - https://leetcode.com/problems/maximum-depth-of-binary-tree/ ✅
	5. Find diameter of a binary Tree(ii) - https://leetcode.com/problems/diameter-of-binary-tree/ ✅
		- also try and get the path of the maximum diamter ✅
	6. Invert a binary Tree(ii) - https://leetcode.com/problems/invert-binary-tree/ ✅
	7. All nodes at distance k in a binary tree(iii) - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/   🚫
	8. Max path sum(iv) - https://leetcode.com/problems/binary-tree-maximum-path-sum/ - ✅
	9. Difference between node and ancestor(v) https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/  ✅
	10. Sum of node when even valued grand parent(v) - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/ 
	11. Binary Tree Camera(v) - https://leetcode.com/problems/binary-tree-cameras/description/ 🚫
	12. Binary Tree Coloring game(v) - https://leetcode.com/problems/binary-tree-coloring-game/description/🚫 
	13. Distribute Coins in Binary Tree (v) - https://leetcode.com/problems/distribute-coins-in-binary-tree/description/ 🚫
	14. https://leetcode.com/problems/count-complete-tree-nodes/ 🚫

- Count Complete Tree Nodes https://leetcode.com/problems/count-complete-tree-nodes/ 
-  Closest Binary Search Tree Value - https://leetcode.com/problems/closest-binary-search-tree-value/
-  Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root. The boundary includes left boundary, leaves, and right boundary in order without duplicate nodes. (The values of the nodes may still be duplicates.)

The left boundary is defined as the path from the root to the left-most node. The right boundary is defined as the path from the root to the right-most node. If the root doesn’t have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not apply to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if it exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined in the same way with left and right exchanged.
For example, boundary traversal of the following tree is “20 8 4 10 14 25 22”
![Pasted_image_20201006201421](/processed/images/Pasted_image_20201006201421.png)


2. Abstract Data Type ?
4. What is sorting in place ?


Problems
- there might be a issue with binary_tree/balanced_tree.py  
- https://github.com/archana15/Algorithms/pull/12/files#diff-7cdbac197b3e646b49775c47bfa006e5R94

- binary_tree/max_width.py 
	- what is missing here
	- we can do a bfs walk and measure the length of the array ?

https://github.com/archana15/Algorithms/pull/13/files#diff-1ef436fd433292cf7cb2f3d4e9672a51R62 
- this is generally a bad idea, hard to keep track
- instead create nodes and then do left of right, may be this is easier for smaller problems but if the depth were to increase this might get hard
