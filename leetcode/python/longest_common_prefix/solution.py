class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ''
        minl = min(len(s) for s in strs)
        i = 0
        while i < minl:
            for n in range(1, len(strs)):
                if strs[n][i]!=strs[0][i]:
                    return strs[0][:i]
                
            i += 1  
        return strs[0][:i]