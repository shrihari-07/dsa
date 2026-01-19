"""
930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""

from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        summ_freq = defaultdict(int)
        summ_freq[0] = 1
        count = 0
        summ = 0

        for num in nums:
            summ += num

            if summ - goal in summ_freq:
                count += summ_freq[summ - goal]
            
            summ_freq[summ] += 1
        
        return count
