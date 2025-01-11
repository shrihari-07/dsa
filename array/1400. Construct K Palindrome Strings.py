"""
1400. Construct K Palindrome Strings
https://leetcode.com/problems/construct-k-palindrome-strings

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
 
Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
"""

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        if len(s) == k:
            return True
        
        odd_count = 0
        freq_dict = Counter(s)
        for key, value in freq_dict.items():
            if freq_dict[key] % 2 != 0:
                odd_count += 1

        if odd_count > k:
            return False

        return True
