class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            elif s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            elif s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False # There is more left parentheses
        else:
            return True