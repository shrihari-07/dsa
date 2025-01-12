"""
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = 9999999
        nums.sort()

        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                three_sum = nums[start] + nums[i] + nums[end]
                if abs(three_sum - target) < abs(closest_sum - target):
                    closest_sum = three_sum
                if three_sum < target:
                    start += 1
                elif three_sum > target:
                    end -= 1
                else:
                    return three_sum
        
        return closest_sum
