class Solution(object):
    def DFS(self, n, k, start, list):
        if len(list) == k:
            self.res.append(list[:])
            return
        for i in range(start, n+1):
            list.append(i)
            self.DFS(n, k, i+1,list)
            list.pop()
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        self.res = []
        self.DFS(n, k, 1, [])
        return self.res