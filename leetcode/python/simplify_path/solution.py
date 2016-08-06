class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0 
        while i < len(path):
            end = i+1
            while end < len(path) and path[end] != '/':
                end += 1
            newL = path[i+1:end]
            if len(newL) > 0:
                if newL == '..':
                    if stack != []:     #Must right this!!!!!!!!
                        stack.pop()
                elif newL != '.':
                    stack.append(newL)
            i = end
        if stack == []:
            return "/"
        s = ''
        for i in stack:
            s += '/' + i
        return s