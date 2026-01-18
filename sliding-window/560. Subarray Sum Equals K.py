"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        summ = 0

        for num in nums:
            summ += num

            if summ - k in sum_freq:
                count += sum_freq[summ-k]
            
            sum_freq[summ] += 1
        
        return count
