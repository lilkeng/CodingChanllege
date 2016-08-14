# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = None; self.n2 = None
        self.prev = None
        self.findTwoNode(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        
    def findTwoNode(self, root):
        if root == None:
            return root
        else:
            self.findTwoNode(root.left)
            if self.prev != None and self.prev.val > root.val:
                self.n2 = root
                if self.n1 == None:
                    self.n1 = self.prev
            self.prev = root
            self.findTwoNode(root.right)
            
            
            
            