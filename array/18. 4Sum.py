"""
18. 4Sum
https://leetcode.com/problems/4sum/

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    four_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if four_sum == target:
                        res.add((nums[i], nums[j], nums[start], nums[end]))
                        start += 1
                        end -= 1
                    elif target > four_sum:
                        start += 1
                    else:
                        end -= 1
        
        return [list(i) for i in res]
