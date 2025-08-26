"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
"""

# Traversal: left -> right -> root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursiveTraversal(root):
            if root is None:
                return []
            left_values = recursiveTraversal(root.left)
            right_values = recursiveTraversal(root.right)
            return [*left_values, *right_values, root.val]
        
        return recursiveTraversal(root)
