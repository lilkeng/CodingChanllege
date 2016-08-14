# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.validBST(root)
    
    def validBST(self, root):
        if root == None:
            return True
        else:
            if not self.validBST(root.left):
                return False
            #For now self.prev is the root.left
            #It was assigned in the above recursion step
            if self.prev != None:
                if self.prev.val >= root.val:
                    return False
            self.prev = root
            if not self.validBST(root.right):
                return False
        return True
                    
                    
                    
                    