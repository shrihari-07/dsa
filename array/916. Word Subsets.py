"""
916. Word Subsets
https://leetcode.com/problems/word-subsets

You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order.


Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
"""

from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        max_freq = Counter()
        
        for word2 in words2:
            for key, value in Counter(word2).items():
                max_freq[key] = max(max_freq[key], value)
        
        for word1 in words1:
            c_word1 = Counter(word1)
            if max_freq <= c_word1:
                res.append(word1)
        
        return res
