"""
3174. Clear Digits
https://leetcode.com/problems/clear-digits/

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:
- Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        i = 0
        res = ""
        s_list = list(s)

        while i < len(s_list):
            if s_list[i].isnumeric():
                s_list[i] = "#"
                for j in range(i - 1, -1, -1):
                    if s_list[j].isalpha():
                        s_list[j] = "#"
                        break
            i += 1
        
        for i in range(len(s_list)):
            if s_list[i] != "#":
                res += s_list[i]
        
        return res
