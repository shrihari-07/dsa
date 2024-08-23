"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        count = 0

        for parantheses in s:
            if parantheses == "(" or parantheses == "[" or parantheses == "{":
                count += 1
                stack.append(parantheses)
            elif len(stack) != 0:
                closing_parantheses = stack.pop()
                if (parantheses == ")" and closing_parantheses != "(") \
                    or (parantheses == "]" and closing_parantheses != "[") \
                        or (parantheses == "}" and closing_parantheses != "{"):
                    return False
            else:
                return False

        if len(stack) == 0 and count != 0:
            return True
        
        return False
