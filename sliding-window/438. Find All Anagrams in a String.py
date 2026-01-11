"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)

        if m < n:
            return []
        
        s_freq = defaultdict(int)
        p_freq = defaultdict(int)
        result = []
        left = 0

        for i in range(n):
            s_freq[s[i]] += 1
            p_freq[p[i]] += 1
        
        if s_freq == p_freq:
            result.append(0)
        
        for right in range(n, m):
            s_freq[s[right]] += 1
            s_freq[s[left]] -= 1

            if s_freq[s[left]] == 0:
                del s_freq[s[left]]
            
            left += 1

            if s_freq == p_freq:
                result.append(left)
        
        return result
