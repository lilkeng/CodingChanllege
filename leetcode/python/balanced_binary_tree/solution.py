# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def getHeight(self, root):
        if root == None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
            
        
            