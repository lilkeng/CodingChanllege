class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        last = -1
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxLen = max(maxLen, i - last)
                    else:
                        maxLen = max(maxLen, i - stack[len(stack)-1])
        return maxLen