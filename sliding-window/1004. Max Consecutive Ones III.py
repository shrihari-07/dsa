"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

from collections import defaultdict

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        max_freq = 0
        left = 0
        max_num = 0

        for right in range(n):
            freq[nums[right]] += 1
            max_freq = max(max_freq, freq[1])
            max_num = right - left + 1

            while max_num - max_freq > k:
                freq[nums[left]] -= 1
                left += 1
                max_num = right - left + 1
        
        return max_num
