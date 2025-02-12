"""
2342. Max Sum of a Pair With Equal Sum of Digits
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
"""

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_dict = {}
        max_value = -1

        for num in nums:
            digit_sum = 0
            digits = list(str(num))
            for digit in digits:
                digit_sum += int(digit)
            
            if digit_sum not in digit_sum_dict:
                digit_sum_dict[digit_sum] = []
            digit_sum_dict[digit_sum].append(num)
        
        for key in digit_sum_dict:
            n = len(digit_sum_dict[key])
            if n > 1:
                digit_sum_dict[key].sort()
                sum = digit_sum_dict[key][n-1] + digit_sum_dict[key][n-2]
                max_value = max(max_value, sum)
        
        return max_value
