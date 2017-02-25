'''
LeetCode

Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if
the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and
"([)]" are not.

'''

class Solution(object):
    def isValid(self, s):
        stack = []
        p = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in p.values():
                stack.append(c)
            elif c in p.keys():
                if stack == [] or p[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []
