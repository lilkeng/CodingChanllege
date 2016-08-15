# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.levelBST(root, 0, res)
        res.reverse()
        return res
    
    def levelBST(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            self.levelBST(root.left, level+1, res)
            self.levelBST(root.right, level+1, res)