"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters 
may map to the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    return False
            elif t[i] != mapping[s[i]]:
                return False
        return True
