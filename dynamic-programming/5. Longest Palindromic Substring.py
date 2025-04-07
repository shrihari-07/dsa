"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        def check_palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        for i in range(len(s)):
            odd_palindrome = check_palindrome(i, i)
            even_palindrome = check_palindrome(i, i + 1)

            if len(odd_palindrome) > max_len:
                max_len = len(odd_palindrome)
                res = odd_palindrome
            
            if len(even_palindrome) > max_len:
                max_len = len(even_palindrome)
                res = even_palindrome
        
        return res
