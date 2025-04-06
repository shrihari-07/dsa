"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# Tabulation
class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * (n + 2)
        table[0] = 0
        table[1] = 1

        for i in range(len(table)):
            if (i + 1) < len(table):
                table[i + 1] += table[i]
            if (i + 2) < len(table):
                table[i + 2] += table[i]

        return table[n + 1]


# Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def calculate_fib(n):
            if n in memo:
                return memo[n]
        
            memo[n] = calculate_fib(n - 1) + calculate_fib(n - 2)
            return memo[n]

        return calculate_fib(n + 1)
