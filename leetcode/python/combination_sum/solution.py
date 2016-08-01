class Solution(object):
    def DFS(self, candidates, target, start, list):
        length = len(candidates)
        if target == 0:
            return Solution.res.append(list)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, list + [candidates[i]])
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.res = []
        self.DFS(candidates, target, 0, [])
        return Solution.res