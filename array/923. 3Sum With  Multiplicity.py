"""
923. 3Sum With Multiplicity
https://leetcode.com/problems/3sum-with-multiplicity/

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Example 3:
Input: arr = [2,1,3], target = 6
Output: 1
Explanation: (1, 2, 3) occured one time in the array so we return 1.
"""

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        count = 0
        visited = set()
        arr.sort()

        for i in range(n):
            start = i + 1
            end = n - 1
            while start < end:
                three_sum = arr[i] + arr[start] + arr[end]
                if three_sum == target:
                    visited.add((arr[i], arr[start], arr[end]))
                    start += 1
                    end -= 1
                elif three_sum < target:
                    start += 1
                else:
                    end -= 1
        
        for i, j, k in visited:
            if i < j < k:
                count += arr.count(i) * arr.count(j) * arr.count(k)
            elif i == j == k:
                count += arr.count(i) * (arr.count(i) - 1) * (arr.count(i) - 2) // 6
            elif i == j != k:
                count += arr.count(i) * (arr.count(i) - 1) * arr.count(k) // 2
            elif i != j == k:
                count += arr.count(j) * (arr.count(j) - 1) * arr.count(i) // 2
        
        return count % (10**9 + 7)
