"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for i in range(len(s)):
            s_freq[s[i]] += 1
        
        for i in range(len(t)):
            t_freq[t[i]] += 1
        
        for key in s_freq:
            if s_freq[key] != t_freq.get(key, 0):
                return False

        for key in t_freq:
            if t_freq[key] != s_freq.get(key, 0):
                return False
        
        return True
