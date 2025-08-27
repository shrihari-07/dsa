"""
993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_flag = False
        y_flag = False
        x_parent = 0
        y_parent = 0
        queue = deque([ (0, root) ])

        while queue and root:
            for _ in range(len(queue)):
                parent, node = queue.popleft()
                if node.val == x:
                    x_flag = True
                    x_parent = parent
                elif node.val == y:
                    y_flag = True
                    y_parent = parent
                
                if node.left:
                    queue.append((node, node.left))
                if node.right:
                    queue.append((node, node.right))
            
            if x_flag and y_flag:
                if x_parent != y_parent:
                    return True
                return False
            
            if x_flag or y_flag:
                return False
        
        return False
