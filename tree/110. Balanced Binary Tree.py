"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [ root ]
        heights = defaultdict(int)
        node = root
        last_visited = None

        while stack and root:
            while node:
                stack.append(node)
                node = node.left
            
            peek_node = stack[-1]
            if peek_node.right and peek_node.right != last_visited:
                node = peek_node.right
            else:
                left_height = heights[peek_node.left]
                right_height = heights[peek_node.right]
                if abs(left_height - right_height) > 1:
                    return False
                heights[peek_node] = max(left_height, right_height) + 1
                last_visited = stack.pop()
        
        return True
