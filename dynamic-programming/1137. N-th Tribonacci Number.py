"""
1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
"""

# Tabulation
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
            
        table = [0] * (n + 1)
        table_len = len(table)
        table[0] = 0
        table[1] = 1

        for i in range(table_len):
            if i + 1 < table_len:
                table[i + 1] += table[i]
            if i + 2 < table_len:
                table[i + 2] += table[i]
            if i + 3 < table_len:
                table[i + 3] += table[i]
        
        return table[n]


# Memoization
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        
        def calc_trib(n):
            if n in memo:
                return memo[n]
            
            memo[n] = calc_trib(n - 1) + calc_trib(n - 2) + calc_trib(n - 3)
            return memo[n]
        
        return calc_trib(n)
