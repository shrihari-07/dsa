"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)
        
        return is_mirror(root.left, root.right)


from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([ (root.left, root.right) ])

        while queue and root:
            n1, n2 = queue.popleft()

            if n1 is None and n2 is None:
                continue
            
            if n1 is None or n2 is None:
                return False

            if n1.val != n2.val:
                return False
            
            queue.append((n1.left, n2.right))
            queue.append((n1.right, n2.left))

        return True
