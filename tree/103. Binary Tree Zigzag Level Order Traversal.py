"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        switch = False
        output = []
        queue = deque([ root ])

        while queue and root:
            level_output = []
            for i in range(len(queue)):
                if not switch:
                    r = queue.popleft()
                    level_output.append(r.val)
                    if r.left: queue.append(r.left)
                    if r.right: queue.append(r.right)
                else:
                    r = queue.pop()
                    level_output.append(r.val)
                    if r.right: queue.appendleft(r.right)
                    if r.left: queue.appendleft(r.left)
            switch = not switch
            output.append(level_output)
        
        return output
