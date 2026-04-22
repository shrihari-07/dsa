"""
1721. Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        prev_left = start
        prev_right = start
        left = head
        right = head

        for i in range(k - 1):
            prev_left = left
            left = left.next
        
        temp = left
        while temp.next:
            prev_right = right
            right = right.next
            temp = temp.next
        
        if left == right:
            return head
        
        prev_left.next, prev_right.next = right, left
        left.next, right.next = right.next, left.next

        return start.next
