```python
class Solution(object):
     tsum = 0

     def evenGrandparent(self, root, parent = 1, grandparent = 1):
         if root:
             if grandparent % 2 == 0:
                 self.tsum += root.val 
                 # self.tsum = self.tsum + root.val
             # print('\n') 
             # print('node = '+str(root.val))
             # print('parent = '+str(parent))
             # print('grandparent = '+str(grandparent))
             # print(self.tsum)
             self.evenGrandparent(root.left, root.val, parent)  # node, parent, grandparent
             self.evenGrandparent(root.right, root.val, parent)  

     def sumEvenGrandparent(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         # tsum = 0

         self.evenGrandparent(root)
         return self.tsum 
 ```
 
 This solution is somewhat complicated and not very nice to read
 
 probably the other way of solving that would be 
 ```
 class Solution:
    
    def even_sum(self, subtree, parent, grandparent):
        if subtree is None:
            return 0
        else:
            l = self.even_sum(subtree.left, subtree.val, parent)
            r = self.even_sum(subtree.right, subtree.val, parent)
            if grandparent is not None and grandparent % 2 == 0:
                return l+r + subtree.val
            else:
                return l+r
        
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.even_sum(root, None, None)
```

which is much nicer and easy to understand and write and build upon the previous concepts that we have learnt while doing maxpath sum 


writing a tail recursive solution of this problem might not be very ideal for this, the attempted thing was

```
class Solution:
    
    def even_sum(self, subtree, parent, grandparent, evensum):
        if subtree is None:
            return 0
        if subtree.left is None and subtree.right is None:
            if grandparent and grandparent % 2 == 0:
                return evensum + subtree.val
            else:
                return evensum
        else:
            if grandparent is not None and grandparent % 2 == 0:
                newevensum =  evensum +  subtree.val
            else:
                newevensum = evensum
                
            return self.even_sum(subtree.left, subtree.val, parent, newevensum) + self.even_sum(subtree.right, subtree.val, parent, newevensum)
        
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.even_sum(root, None, None, 0)
```


This bit of code, makes the paths come out twice and will lead to double counting
And very dangerous when we are going sum or multiplication 
This makes me think that using a tail recursive solution for trees for other than accumulation might lead to bad solution 
```python       

        if subtree is None:
            return evensum
        if subtree.left is None and subtree.right is None:
            if grandparent and grandparent % 2 == 0:
                return evensum + subtree.val
            else:
                return evensum
				
				
```


Notes about https://github.com/archana15/Algorithms/blob/1bb257e8c49e673d9da36cabc6e0e0971acb76e5/binary_tree/closest_bst_value.py