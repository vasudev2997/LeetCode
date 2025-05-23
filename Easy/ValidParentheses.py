# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, strs_inp):
        stack = []
        bracket_map = {")":"(", "]":"[", "}":"{"}
        for char in strs_inp:
            if char in bracket_map.values():
                stack.append(char)
            elif len(stack)>=1 and bracket_map[char]==stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
