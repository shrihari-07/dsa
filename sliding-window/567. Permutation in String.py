"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)

        for i in range(len(s1)):
            s1_freq[s1[i]] += 1
            s2_freq[s2[i]] += 1
        
        if s1_freq == s2_freq:
            return True
        
        left = 0
        for right in range(m, n):
            s2_freq[s2[right]] += 1
            s2_freq[s2[left]] -= 1

            if s2_freq[s2[left]] == 0:
                del s2_freq[s2[left]]
            
            if s1_freq == s2_freq:
                return True
            
            left += 1
        
        return False
